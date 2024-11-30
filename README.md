     IOT AUTOMATED WATER DISPENSER.

Group 1 members 

Farouk Rashid.

Mathew Muthee.

Bernard Ochieng.

Daisy Nyamori.

Micheal otieno

Christine Juma

      OVERVIEW.
This IoT project aim to develop a smart water tap that automatically control water flow boud on hand proximity By utilizing a proximity server, the top will dispense water only when a band is detected, thereby conserving water and promoting hygiene

Components

* Microcontroller: Rasberry Pi

* Proximity senior;Detects presence of hand near the tap

* Relay module; controls flow of electricity to the water valve

* Water valve; control water flow

* Water dispenser; water flows form the tap

* Benefits of this project to the community.

* Water conservation.Significance reduction in water westage

* Improves Hygiene. Minimizes physical contact us the tap.

* The database will be stening the following data from the water sensor;

* waterflow. In boolean form that is, on and off

* Timestamp - time at which data was recorded

   Operation:

* When a hand is placed near the ultrasonic sensor, the sensor detects the object and sends a signal to the Raspberry pi.
   
* The Raspberry pi processes the signal and calculates the distance.
   
* If the distance is within the set threshold, the Raspberry pi activates, the relay which in turn switches on the water pump.
  
* Water is dispensed until the hand is removed.
  
* Once the hand is removed, the sensor no longer detects the object, and the Raspberry pi deactivates the relay, stopping the water flow.

    Steps:
1. GPIO Pin Setup: Configures the GPIO pins for the trigger, echo, and relay.

![Configuration of the pins](https://github.com/user-attachments/assets/7262bb64-5ca9-4e49-adf1-14fc9eeab8a7)


2. Connections: connect the jumper cables on the the Raspberry Pi and to the bread board on the pump and to the proximity sensor.
   connect also the jumper cables to the ground and power source of the Raspberry Pi and back to the breadboard.

![Connection of the jumper cables](https://github.com/user-attachments/assets/060b69a6-2151-498c-bd0b-b786cc8b265a)

   
4. Pump Control: If the distance is less than a certain threshold, the relay is activated to turn on the pump. Otherwise, the pump is turned off.
   
5. Loop: Continuously measures the distance and controls the pump.
  
