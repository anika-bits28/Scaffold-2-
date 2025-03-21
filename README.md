
# Moving Waves & Ship Diorama  

## Project Overview  
This project is a small-scale, interactive diorama that simulates ocean waves and a rocking ship using servo motors. A touch sensor activates the system, while NeoPixel LEDs create an animated water effect with different shades of blue.  

## How It Works  
- Touching the sensor activates the system.  
- One servo motor moves a set of paper waves up and down.  
- Another servo motor rocks a small paper ship side to side.  
- NeoPixel LEDs cycle through shades of blue to create a dynamic ocean effect.  
- When the touch sensor is not activated, the system remains idle.  

## Components Used  
| Component | Purpose |  
|-----------|---------|  
| ESP32 | Microcontroller to control all components |  
| 2x Servo Motors | Moves waves and rocks the ship |  
| 1x Touch Sensor | Turns the scene on and off |  
| NeoPixel LED Strip | Creates the animated water effect |  
| Paper & Cardboard | Used to craft the waves and boat |  

## Wiring Guide  
| Component | ESP32 Pin |  
|-----------|----------|  
| Touch Sensor | GPIO 32 |  
| Servo 1 (Waves) | GPIO 22 |  
| Servo 2 (Boat) | GPIO 26 |  
| NeoPixel LED Data | GPIO 5 |  

## Code Breakdown  
The script runs a loop that continuously checks for touch sensor input:  
1. If the sensor is touched:  
   - The waves begin moving back and forth.  
   - The boat tilts left and right.  
   - The LEDs transition through blue ocean colors.  

2. If the sensor is not touched:  
   - All movement stops.  
   - LEDs turn off.  

## How to Use  
1. Power on the ESP32.  
2. Touch the sensor to activate the diorama.  
3. Touch again to stop all movement.  
4. Modify the colors and movement settings in the code to customize the effect.  

## Future Upgrades  
- Add a storm mode with faster wave motion and flashing lights.  
- Use a buzzer to generate ocean sounds.  
- Create a sunset effect with warm LED colors.  

## How to Upload Code to ESP32  
1. Open MU Editor. 
2. Connect the ESP32 via USB.  
3. Copy and paste the `.py` file into the editor.  
4. Click "Run" to execute the script.  

