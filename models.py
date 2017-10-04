from google.appengine.ext import ndb
# default property should be string for all prperties except date and user
# because its easy to manipulate and work well with html forms


class Prices(ndb.Model):
    date = ndb.DateTimeProperty()
    name = ndb.StringProperty()
    gujarati_name = ndb.StringProperty()
    product_id = ndb.StringProperty()
    price = ndb.StringProperty()
    unit = ndb.StringProperty()
    user = ndb.UserProperty(auto_current_user_add=True)
    created = ndb.DateTimeProperty(auto_now_add=True)


class Products(ndb.Model):
    name = ndb.StringProperty()
    price = ndb.StringProperty()
    quntity = ndb.StringProperty(default='0')
    total = ndb.StringProperty(default='0')
    user = ndb.UserProperty(auto_current_user_add=True)
    created = ndb.DateTimeProperty(auto_now_add=True)


class Admins(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    user = ndb.UserProperty(auto_current_user_add=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

class Shops(ndb.Model):
    name = ndb.StringProperty()
    owner = ndb.StringProperty()
    number = ndb.StringProperty()
    village = ndb.StringProperty()
    user = ndb.UserProperty(auto_current_user_add=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

class Orders(ndb.Model):
    shop_id = ndb.StringProperty()
    shop_owner = ndb.StringProperty()
    shop_number = ndb.StringProperty()
    shop_village = ndb.StringProperty()
    customer_id = ndb.StringProperty()
    customer_name = ndb.StringProperty()
    customer_gujarati_name = ndb.StringProperty()
    date = ndb.DateTimeProperty()
    user = ndb.UserProperty(auto_current_user_add=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    product_name = ndb.StringProperty()
    product_gujarati_name = ndb.StringProperty()
    quntity = ndb.StringProperty()
    price = ndb.StringProperty()
    calculated_price = ndb.StringProperty()

class Customers(ndb.Model):
    name = ndb.StringProperty()
    gujarati_name = ndb.StringProperty()
    shop_id = ndb.StringProperty()
    shop_number = ndb.StringProperty()
    shop_owner = ndb.StringProperty()
    shop_village = ndb.StringProperty()



# class GstBillHead(ndb.Model):
#     buyer_order_no = ndb.StringProperty()
#     created = ndb.DateTimeProperty(auto_now_add=True)
#     customer_address = ndb.TextProperty()
#     customer_gstin = ndb.StringProperty()
#     customer_name = ndb.StringProperty()
#     customer_pincode = ndb.StringProperty()
#     delivery_note = ndb.TextProperty()
#     despatch_doc_date = ndb.DateTimeProperty()
#     despatch_doc_no = ndb.StringProperty()
#     despathed_through = ndb.StringProperty()
#     destination = ndb.StringProperty()
#     destination_state_code = ndb.StringProperty()
#     invoice_date = ndb.DateTimeProperty()
#     invoice_number = ndb.StringProperty()
#     my_company_address = ndb.TextProperty()
#     my_company_gstin = ndb.StringProperty()
#     my_company_name = ndb.StringProperty()
#     my_company_pincode = ndb.StringProperty()
#     order_date = ndb.DateTimeProperty()
#     terms_of_delivery = ndb.TextProperty()
#     terms_of_payment = ndb.TextProperty()
#     user = ndb.UserProperty(auto_current_user_add=True)
#     user_id = ndb.StringProperty()


# class Users(ndb.Model):
#     address = ndb.TextProperty()
#     created = ndb.DateTimeProperty(auto_now_add=True)
#     first_name = ndb.StringProperty()
#     last_name = ndb.StringProperty()
#     phone_number = ndb.StringProperty()
#     user = ndb.UserProperty(auto_current_user_add=True)


# class Accounts(ndb.Model):
#     """
#     account_type will be my_company while creating company for user
#     and customer while creating a customer
#     """
#     address = ndb.TextProperty()
#     # we are storing the company id as StringProperty because we are getting it
#     # through html form as string and string is very flexible compared to int
#     company_id = ndb.StringProperty()
#     created = ndb.DateTimeProperty(auto_now_add=True)
#     email = ndb.StringProperty()
#     gstin = ndb.StringProperty()
#     name = ndb.StringProperty()
#     phone_number = ndb.StringProperty()
#     pincode = ndb.StringProperty()
#     account_type = ndb.StringProperty()
#     user = ndb.UserProperty(auto_current_user_add=True)


# class GstBillBody(ndb.Model):
#     amt = ndb.StringProperty()
#     bill_id = ndb.StringProperty()
#     description = ndb.StringProperty()
#     hsn = ndb.StringProperty()
#     per = ndb.StringProperty()
#     qnt = ndb.StringProperty()
#     rate = ndb.StringProperty()
