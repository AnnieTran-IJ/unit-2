# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
In the common laundry area in R4-Up and R3-10, students frequently report that their clothes come out damp from the dryer, requiring multiple cycles to dry fully. This problem is especially noticeable during the winter when colder temperatures and higher humidity seem to affect the drying process. Residents suspect that the environmental conditions in the laundry room—such as low temperature or high humidity—are interfering with the dryer’s performance, but they lack the data to confirm this or identify effective solutions.

To address this, the students look for a low-cost sensing device to monitor temperature and humidity in the laundry area over a week. By analyzing the collected data, they aim to determine if environmental factors are contributing to the issue and propose targeted solutions, such as improving ventilation, adjusting room insulation, or optimizing dryer settings. 

## Proposed Solution
Considering the client's requirements an adequate solution includes a low-cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired. For a low-cost sensing device, an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequate precision and range for the client's requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20, or the AM2301B [^2] have higher specifications, however, the DHT11 uses a simple serial communication (SPI) rather than more elaborated protocols such as the I2C used by the alternatives. For the range, precision, and accuracy required in this application, the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often-used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In addition to the low cost of the Arduino (< 6USD), this device is programable and expandable[^1]. I considered alternatives such as different versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constraints of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a high-level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is the responsibility of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition, an HLL language will allow me and future developers to extend the solution or solve issues promptly.  

**Design statement:** We will develop a system using Arduino and DHT11 sensors to measure temperature and humidity at 3 different locations in the laundry area in R4U and R3-10, as specified by the client. The system will use Python for data processing and visualization, implemented in the PyCharm IDE. Collected data will be visualized using the pyplot module from Python's matplotlib library to provide clear insights into the environmental conditions within the room.

## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

1. The solution provides a visual representation of the Humidity, Temperature, and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of a minimum of 48 hours.
- **Issues tackled:** This solution helps solve the shortage of insight into the environmental conditions over time, both inside and outside the dormitory, which could help in identifying patterns or irregularities.
2. ```[HL]``` The local variables will be measured using a set of 3 sensors around the dormitory.
- **Issues tackled:** Data collection can be spatially distributed to accurately reflect variations in environmental conditions across different areas of the dormitory.
3. The solution provides mathematical modeling for the Humidity, Temperature, and atmospheric pressure (HL) levels for each Local and Remote location. ```(SL: linear model)```, ```(HL: non-linear model)``` ```
- **Issues tackled:** This solution resolves the difficulty in understanding the relationships between variables and the need for precise modeling to predict how these factors interact locally and remotely.
4. The solution provides a comparative analysis of the Humidity, Temperature, and atmospheric pressure (HL) levels for each Local and Remote location including mean, standard deviation, minimum, maximum, and median. 
- **Issues tackled:** This solution helps assess variability and identify extreme values or trends.
5. ```(SL)```The local samples are stored in a CSV file and ```(HL)``` posted to the remote server as a backup. 
- **Issues tackled:** This solution resolves the risk of data loss and lack of organized storage and accessibility for collected data over time.
6. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL).
- **Issues tackled:** This solution offers predictive insights into upcoming environmental changes, which could help in proactive decision-making.
7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature, and atmospheric pressure (HL).
- **Issues tackled:** This solution resolves the challenge of a consolidated summary to communicate findings, models, and recommendations effectively, preventing informed actions based on the analysis.

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change?_

**1. How does our use of technology shape our understanding of the environment?**
  Technology uncovers patterns and trends, such as rising global temperatures and shifting weather patterns, that would be impossible to detect through observation alone. Predictive models, satellite imaging, and machine learning provide insights into the causes and impacts of climate change, guiding policy and action. This technological lens allows us to grasp the scale and complexity of environmental issues more clearly than ever before.
  
  However, the use of data science raises critical questions, such as "How do we account for biases in data collection and limitations in models that might skew findings?" "Are interpretations of data shaped by human or algorithmic assumptions, and how does this affect conclusions?" Ethical concerns occur when data is used selectively or disproportionately to influence policies, potentially marginalizing certain communities.

**2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?** 
  In the context of our project, we must ensure the privacy of individuals by anonymizing any collected data and being transparent about how it is used. Users should give informed consent for the monitoring process, knowing exactly what data is being collected and for what purpose. Security measures such as encryption and secure storage must be implemented to protect the data from unauthorized access. Additionally, we should adhere to data minimization, collecting only the environmental information necessary to improve living conditions without compromising personal privacy.

**3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus?**
  One of the key factors is the perception of comfort, which can vary depending on cultural backgrounds; for example, individuals from warmer climates may tolerate higher temperatures and humidity better than those from cooler regions. Additionally, occupancy patterns in different parts of the campus, such as dormitories versus study buildings, can create variability in readings, as higher foot traffic or different uses of space may influence temperature and humidity levels.

  Contextual elements like building design and maintenance also play a role, as older buildings may have poorer insulation or ventilation, messing up the comparison with newer or better-maintained structures. The timing of the readings is another important factor; environmental conditions may differ between daytime and nighttime due to varying activities or heating schedules. Finally, expectations and biases among users can affect interpretation, as individuals may attribute discomfort to specific factors (e.g., blaming humidity over temperature) based on personal experiences or assumptions, even if the data suggests otherwise. 
# Criteria B: Design
![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.2** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data on our campus. Physical variables were measured with a network of DHT11/BMP280 sensors locally. A remote server provides an API for remote monitoring and storage via the ISAK-S network. 
## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the Problem definition, Design Statement and modify the success criteria | Finalize problem definition and success criteria                  | 10min         | Nov 23                 | A         |
| 2       | Answer TOK connection | Draft and refine answers            | 15min         | Nov 23                 | A         |

## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration