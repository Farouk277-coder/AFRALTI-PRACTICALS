     IDT AUTOMATED WATER DISPENSER.

Group members

Farouk Rashid.

Mathew Muthee.

Bernard Ochieng.

Daisy Nyamori.

Micheal

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

    Steps:
1. GPIO Pin Setup: Configures the GPIO pins for the trigger, echo, and relay.

2. Connections: connect the jumper cables on the the Raspberry Pi and to the bread board on the pump and to the proximity sensor.
   connect also the jumper cables to the ground and power source of the Raspberry Pi and back to the breadboard.
   
3. Pump Control: If the distance is less than a certain threshold, the relay is activated to turn on the pump. Otherwise, the pump is turned off.
  
