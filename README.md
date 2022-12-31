# T-Oscilloscope
This program simulates how a **Cathode-ray tube (CRT)** should work and provides an easy way to play with voltages (fake) and see the results.
It has a modern UI made with customtkinter.

**This project is inspired from [CRT-simulator by TheJMPZ](https://github.com/TheJPMZ/CRT-simulator)**

## Download
[<img src="https://img.shields.io/badge/DOWNLOAD-T Oscilloscope-informational?&color=purple&logo=Python&logoColor=yellow&style=for-the-badge"  width="300">](https://github.com/Akascape/T-Oscilloscope/archive/refs/heads/main.zip)

### Requirements
- Tkinter
- [CustomTkinter](https://pypi.org/project/customtkinter/)
- [TkDial](https://pypi.org/project/tkdial/)
- Turtle

# GUI
![1x](https://user-images.githubusercontent.com/89206401/202371943-b5547b07-1801-4c02-8c7d-46f37892c56f.png)
![2x](https://user-images.githubusercontent.com/89206401/202371959-4d481e8f-ef3c-4bb0-94f5-35e0fbf52924.png)
![3x](https://user-images.githubusercontent.com/89206401/202371967-74c9e36c-24a0-4ba3-98d3-ac938fa4c356.png)

## Functionality
There are two modes, which can be switched at any moment. On the first mode, you can select the voltage of the vertical and horizontal plates changing the electron's position. On the second mode, changing the gap between the plates and a relation of frequencies the trajectory of the electron is displayed automatically.

## Demo
The program's main focus is rendering Lissajous curves:
|   |1:1|1:2|1:3|2:3
|-- |--|--|--|--|
| 0 | ![imagen](https://user-images.githubusercontent.com/64183934/137271752-903bb165-2a63-449f-ad76-adb0a122a2c8.png) |![imagen](https://user-images.githubusercontent.com/64183934/137271779-0966bba7-ab18-4091-b5eb-0e6ec1072749.png) |![imagen](https://user-images.githubusercontent.com/64183934/137271798-50332db2-a682-4a6d-b6b1-ed466efa048c.png) | ![imagen](https://user-images.githubusercontent.com/64183934/137271827-852ec96f-93d6-4005-a53a-4c345374a51d.png)
|45 | ![imagen](https://user-images.githubusercontent.com/64183934/137272136-f3641c7b-b934-48bc-beb7-be88509ba367.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272178-05649540-abcd-4cb8-a445-75388eb2783d.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272215-d9409cab-f37f-4e0e-837f-280e24ccdcd3.png)| ![imagen](https://user-images.githubusercontent.com/64183934/137272242-1a1d403b-332a-4fa7-92b0-478994acdc47.png)
|90 | ![imagen](https://user-images.githubusercontent.com/64183934/137272473-300bb16c-15a0-4711-9e1b-0c0bd4b5a487.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272496-417ec018-c343-4946-bdcc-9372b56ca1d8.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272518-b69f5069-ff69-4032-b96b-80593c20df2b.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272545-bea51c0a-e235-4b91-a410-d698b0cbd9aa.png)
|135|![imagen](https://user-images.githubusercontent.com/64183934/137272623-ee658ac1-4365-4efd-9580-9a0d6fcc4a87.png)|![imagen](https://user-images.githubusercontent.com/64183934/137272647-d4fe4b79-3075-4dac-82e0-7e9491126198.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272681-e722ddda-ec8a-45b4-8c23-6c5532acee7e.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272710-1c603bb0-476d-47b2-a9da-9bed0a9f9c7e.png)

Credits to JPMZ for the demo images.

## Conclusion
I made this just as a fun experiment, practicing some UI development in python. The whole UI is made with native **tkinter + customtkinter + turtle graphics**.

[<img src="https://img.shields.io/badge/LICENSE-MIT-informational?&color=yellow&style=for-the-badge" width="100">](https://github.com/Akascape/T-Oscilloscope/blob/main/LICENSE)
