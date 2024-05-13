from ObserverDesignPattern.Publisher.publisher import IphonePublisher, FridgePublisher
from ObserverDesignPattern.Subscriber.subscriber import EmailSubscriber, MobileSubscriber

# Create Publisher
iphone_publisher = IphonePublisher()
fridge_publisher = FridgePublisher()

# Crete subscriber
first_observer = EmailSubscriber()
second_observer = MobileSubscriber()
third_observer = MobileSubscriber()

# Subscriber
iphone_publisher.subscribe(first_observer)
iphone_publisher.subscribe(third_observer)
fridge_publisher.subscribe(second_observer)

# Update IphoneStock
iphone_publisher.update_stock(10)
fridge_publisher.update_stock(2)
iphone_publisher.update_stock(0)

# unsubscribe
iphone_publisher.unsubscribe(third_observer)

iphone_publisher.update_stock(10)