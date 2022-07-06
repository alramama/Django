from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [ path('', views.home, name="home"),]

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }
	return render(request, 'accounts/dashboard.html', context)

{%  extends 'accounts/main.html' %}

{% block content %}

{%  include 'accounts/status.html' %}

<br>

<div class="row">
	<div class="col-md-5">
		<h5>CUSTOMERS:</h5>
		<hr>
		<div class="card card-body">
			<a class="btn btn-primary  btn-sm btn-block" href="">Create Customer</a>
			<table class="table table-sm">
				<tr>
					<th></th>
					<th>Customer</th>
					<th>Phone</th>
				</tr>

				{% for customer in customers %}
					<tr>
						<td><a class="btn btn-sm btn-info" href="{% url 'customer' customer.id %}">View</a></td>
						<td>{{customer.name}}</td>
						<td>{{customer.phone}}</td>
					</tr>
				{% endfor %}

			</table>
		</div>
	</div>

	<div class="col-md-7">
		<h5>LAST 5 ORDERS</h5>
		<hr>
		<div class="card card-body">
			
			<table class="table table-sm">
				<tr>
					<th>Product</th>
					<th>Date Orderd</th>
					<th>Status</th>
					<th>Update</th>
					<th>Remove</th>
				</tr>

				{% for order in orders %}
					<tr>
						<td>{{order.product}}</td>
						<td>{{order.date_created}}</td>
						<td>{{order.status}}</td>
						<td><a class="btn btn-sm btn-info" href="{% url 'update_order' order.id %}">Update</a></td>

						<td><a class="btn btn-sm btn-danger" href="{% url 'delete_order' order.id %}">Delete</a></td>

					</tr>
				{% endfor %}

		
			</table>
		</div>
	</div>

</div>

{% endblock %}
