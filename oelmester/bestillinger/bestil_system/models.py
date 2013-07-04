from django.db import models
import datetime

# Create your models here.

class Packing(models.Model):
    description = models.CharField(max_length=100)
    value = models.FloatField()
    
    def __unicode__(self):
        return self.description
    
    class Admin:
        pass

class Product(models.Model):
    identifier = models.CharField(max_length=50,primary_key=True)
    long_name = models.CharField(max_length=100)
    in_price= models.FloatField()
    sell_price = models.FloatField()
    bottle_type= models.ForeignKey(Packing,related_name='contents')
    bottle_number = models.IntegerField()
    box_type = models.ForeignKey(Packing,null=True,related_name='contents_1')
    num_stocked = models.IntegerField()
    num_ordered = models.IntegerField()
    #category =  models.IntegerField()  #1:oel, 2:Vand, 3:andet
    
    def __unicode__(self):
        return self.identifier
    
    
    
class Client(models.Model):
    contact_person_1= models.CharField(max_length=100)
    person_1_email = models.EmailField(max_length=100,null=True)
    person_1_room = models.CharField(max_length=3,null=True)
    person_1_phone =  models.CharField(max_length=11,null=True)

    contact_person_2 = models.CharField(max_length=100,null=True)
    person_2_email = models.EmailField(max_length=100,null=True)
    person_2_room = models.CharField(max_length=3,null=True)
    person_2_phone =  models.CharField(max_length=11,null=True)

    name = models.CharField(max_length=100) #Gang eller fest
    
    def __unicode__(self):
        return self.name


class ItemList(models.Model):
    number = models.IntegerField()
    item = models.ForeignKey(Product,related_name='ordered_by')
    order= models.ForeignKey('Order',related_name='orderd_in')
    next = models.ForeignKey('self', null=True)
    delivered = models.IntegerField()

    def __unicode__(self):
        return str(self.number)+" "+str(self.item)+" for "+str(self.order)

class Order(models.Model):
    first_item = models.ForeignKey(ItemList,related_name='is_first_item_of',null=True)
    last_item = models.ForeignKey(ItemList,related_name='is_last_item_of',null=True)
    client = models.ForeignKey(Client)
    date = models.DateField(auto_now_add=True)
    #Costs
    total_value= models.FloatField()
    total_packing = models.FloatField()
    total_total = models.FloatField()

    def add_item(self, item_id, item_num):
        if not (Product.objects.filter(identifier=item_id).all()):
            print "Cannot add unknown product."
            return 0
        newitem=ItemList(number=item_num,item=item_id,order=self,delivered=0)
        newitem.save()
        
        if(self.last_item):
            self.last_item.next=newitem
            self.last_item.save()
            self.last_item=newitem
        else:
            self.last_item=newitem
            self.first_item=newitem
        
        self.save()

    def __unicode__(self):
        return self.date.isoformat()+" for "+str(self.client)
