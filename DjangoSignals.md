Ques 1.     By default the django signals are executed synchronosuly, meaning that when the django signals are executed, the connected recievers or functions get executed in the order they were connected.
            We can make the django signals work asynchronously by using 'async def' but we have to make sure that there is no internal conflict between the methods/functions used. This is to prevent any event loops or race conditions/deadlocks.
            Psedudo Code->
            Default (synchronous):
            #Import all the necessary modules/libraries

            #Define a class for sending an email.

            #Define a method for receiver which accepts sender, instances, created
            #Check if the user is new (that is created is true) then trigger the method created in the above class to send a registartion email.

            #Save the request

            Asynchronous:
            #Import all the necessary modules/libraries

            #Define a class for sending an email for successfull registartion for new user

            #Write an asynchronous receiver class using 'async def' and pass the necessary parameters such as sender, instances, created.
            #Check if the user is new, then trigger the method created in the above class to send a registartion confirmation mail to user.

            #Save the request.

Ques 2.     By default the signal and the caller run in the same thread. As soon as the signal is called, all the processes associated are executed synchronosuly, therefore they run on the same thread to achieve this.

Ques 3.     By default the signal and the caller run on the same database transaction. The reason for this is, it maintains consistency and integrity. It also ensures that the transactions are atomic and isolated from each other, while other transactions are being conducted.



