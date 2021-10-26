# import random
#
# from django.contrib.auth import get_user_model
# from seller.models import Products
# import os
#
# def createorders():
#     User = get_user_model()
#     users = User.objects.all()
#     print(users[4])
    # mobile_name=['mob'+str(i) for i in range(1,11)]
    # print(mobile_name)
    # desc='nice well built mobile'
    # price=random.randrange(10000,100000)
    # stock=random.randrange(10,50)
    # category='Mobile'
    # brand=['Lenovo','Oppo','Apple','Samsung','Redmi']
    # ram=[str(i)+' GB' for i in [8,16,32,64]]
    # storage=[str(i)+' GB' for i in [8,16,32,64,128,256]]
    # color=['black','blue','white']
    # offer=random.randrange(0,50)
    # print(desc,price,stock,category,brand,ram,storage,color,offer)
    # order={}
    # order['user']=random.choice(users)
    # order['product_name']=random.choice(mobile_name)
    # order['description']=desc
    # order['price']=price
    # order['stock']=stock
    # order['category']=category
    # order['brand']=random.choice(brand)
    # order['ram']=random.choice(ram)
    # order['storage']=random.choice(storage)
    # order['color']=random.choice(color)
    # order['offer']=offer
    # # print(order)
    # prod=Products.objects.all()
    # order={}
    # print(prod)
    # order['product']=random.choice(prod)
    # order['user']=random.choice(users)
    # order['address']='Cecilia Chapman,711-2880 Nulla St.,Mankato Mississippi 96522,(257) 563-7401'
    # order['seller']=random.choice(users)
    # order['status']=random.choice(['pending','ordered','shipped','delivered'])
    # print(order)
    # return order




# ====================================================================================================

# def createorder(request):
#     User = get_user_model()
#     users = User.objects.all()
#     x = Products()
#     x=Orders()
#     order = createorders()
    # print(order)
    # users = User.objects.get(username='ajith')
    # print(users)
    # x.user = User.objects.get(username='ajith')
    # x.product_name = order['product_name']
    # x.image = 'mob1.png'
    # x.description = order['description']
    # x.price = order['price']
    # x.stock = order['stock']
    # x.category = 'Mobile'
    # x.brand = order['brand']
    # x.ram = order['ram']
    # x.storage = order['storage']
    # x.color = order['color']
    # x.offer = order['offer']
    # x.save()
    # y=Orders()
    # y.product=order['product']
    # y.user=order['user']
    # y.address=order['address']
    # y.seller=order['seller']
    # y.status=order['status']
    # y.save()
    # return render(request, 'createorder.html')