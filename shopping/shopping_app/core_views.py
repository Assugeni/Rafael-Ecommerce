from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import CheckoutForm

from .models import (
    ProductInfo,
    Order,
    OrderItem,
    CheckoutAddress,
    Payment
)

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = OrderItem.objects.filter(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'core/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = OrderItem.objects.filter(user=self.request.user, ordered=False)
        id = self.request.GET.get('id','')
        total = id.split("!")[1]

        context = {
            'form': form,
            'order': order,
            'total':total
        }
        return render(self.request, 'site/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            all_orders = OrderItem.objects.filter(user=self.request.user, ordered=False)

            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                grand_total = self.request.POST.get('grand_total')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                payment_option = form.cleaned_data.get('payment_option')

                checkout = CheckoutAddress.objects.filter(user=self.request.user)
                if checkout.count() == 0:
                    checkout_address = CheckoutAddress(
                        user=self.request.user,
                        street_address=street_address,
                        apartment_address=apartment_address,
                        country=country,
                        zip=zip
                    )
                    checkout_address.save()
                else:
                    checkout_address = CheckoutAddress.objects.get(user=self.request.user)
                    checkout_address.street_address = street_address
                    checkout_address.apartment_address = apartment_address
                    checkout_address.country = country
                    checkout_address.zip = zip
                    checkout_address.save()

                for obj in all_orders:
                    order = OrderItem.objects.get(id=obj.id)
                    order.checkout_address = checkout_address
                    order.save()

                if payment_option == 'S':
                    return redirect('payment', payment_option='stripe',id='AGYUVSGH!'+grand_total+'!SGDDF')
                else:
                    messages.warning(self.request, "Invalid Payment option")
                    return redirect('checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("order-summary")

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = OrderItem.objects.filter(user=self.request.user, ordered=False)
        id = kwargs.get('id')
        grand_total = id.split("!")[1]

        context = {
            'order': order,
            'grand_total':grand_total
        }

        return render(self.request, "core/payment2.html", context)

    def post(self,request, *args, **kwargs):
        # try:
            all_orders = OrderItem.objects.filter(user=self.request.user, ordered=False)


            id = kwargs.get('id')
            amount = id.split("!")[1]

            # assign payment to order
            for obj in all_orders:
                order = OrderItem.objects.get(id=obj.id)
                order.ordered = True
                order.save()

            checkout_address = CheckoutAddress.objects.filter(user=self.request.user)



            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description="test description",
                source= request.POST['stripeToken'],
                shipping={
                    'name': 'test_user',
                    'address': {
                        'line1': checkout_address[0].street_address,
                        'postal_code': checkout_address[0].zip,
                        'city': "",
                        'state': "",
                        'country': checkout_address[0].country,
                    }
                },
            )

            # create payment
            payment = Payment()
            payment.stripe_id = charge['id']
            payment.user = self.request.user
            payment.amount = amount
            payment.save()

            messages.success(self.request, "Success make an order")
            return redirect('/')

        # except stripe.error.CardError as e:
        #     body = e.json_body
        #     err = body.get('error', {})
        #     messages.error(self.request, f"{err.get('message')}")
        #     return redirect('/')
        #
        # except stripe.error.RateLimitError as e:
        #     # Too many requests made to the API too quickly
        #     messages.error(self.request, "To many request error")
        #     return redirect('/')
        #
        # except stripe.error.InvalidRequestError as e:
        #     # Invalid parameters were supplied to Stripe's API
        #     messages.error(self.request, "Invalid Parameter")
        #     return redirect('/')
        #
        # except stripe.error.AuthenticationError as e:
        #     # Authentication with Stripe's API failed
        #     # (maybe you changed API keys recently)
        #     messages.error(self.request, "Authentication with stripe failed")
        #     return redirect('/')
        #
        # except stripe.error.APIConnectionError as e:
        #     # Network communication with Stripe failed
        #     messages.error(self.request, "Network Error")
        #     return redirect('/')
        #
        # except stripe.error.StripeError as e:
        #     # Display a very generic error to the user, and maybe send
        #     # yourself an email
        #     messages.error(self.request, "Something went wrong")
        #     return redirect('/')
        #
        # except Exception as e:
        #     # Something else happened, completely unrelated to Stripe
        #     messages.error(self.request, "Not identified error")
        #     return redirect('/')


@login_required
def add_to_cart(request, pk,quantity):

    item = get_object_or_404(ProductInfo, pk=pk)
    print(quantity)

    order_item, created = OrderItem.objects.get_or_create(
        product_info = item,
        user = request.user,
        ordered = False,
        quantity = quantity
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        new_quantity = 0

        if order.items.filter(product_info__pk=item.pk).exists():
            prv_quantity = int(order_item.quantity)
            new_quantity =  prv_quantity + int(quantity)
            order_item.save()
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("order-summary")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(ProductInfo, pk=pk )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product_info__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                product_info=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \""+order_item.product_info.product_title+"\" remove from your cart")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("product_details", pk=pk)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("product_details", pk = pk)


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(ProductInfo, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("order-summary")