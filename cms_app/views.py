from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, Lead, WalkIn
from .serializers import DeviceSerializer, LeadSerializer, WalkInSerializer
from django.shortcuts import render
from .models import Device, Vendor
from django.core.paginator import Paginator
from . import utilities

class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.filter(status=True)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class LeadCreateView(APIView):
    def post(self, request):
        lead_data_keys=['name','phone_number','email','address','city','referral_code']
        lead_data={key:val for key,val in request.POST.items() if key in lead_data_keys}
        serializer = LeadSerializer(data=lead_data)
        if serializer.is_valid():
            lead = serializer.save()
            # Create WalkIn record with token

            walk_in = WalkIn.objects.create(
                lead=lead,
                vendor=Vendor.objects.get(id = request.data.get('vendor_id')),  # Assign based on logic
                device=Device.objects.get(id = request.data.get('device_id')),  # Assign based on logic
                currency='INR',
                offer_price=0.0,
                token_number=WalkIn.objects.count() + 1,
            )
            # Send email logic here
            # send email to lead
            sender_email = 'sender@domain.com'
            sender_password = 'senderpassword'  #app sepcific password needs to be created
            utilities.send_email(sender_email, sender_password,lead_data['email'],'Thankyou for visiting us', 'Our representative will contact you soon')
            
            # send email to vendor
            vendor_email = Vendor.objects.get(id = request.data.get('vendor_id')).email
            utilities.send_email(sender_email, sender_password,vendor_email,'New lead to your product', 'Lead: lead_id is intereted in your product ')

            return Response({'token': walk_in.token_number}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def home_view(request):
    #devices = Device.objects.filter(status=True)  # 3x4 grid
    device_queryset = Device.objects.all()
    paginator = Paginator(device_queryset, 12)  # 12 devices per page
    page_number = request.GET.get('page', 1)  # Default to the first page
    devices = paginator.get_page(page_number)
    return render(request, 'index.html', {'devices': devices})
