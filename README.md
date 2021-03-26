
<p align="left">
  <img width="1000" src="Assets/GIF1.gif" >
</p>

# Graphical User interface (GUI) for Realtime Drilling Optimization system

### Driling Realtime Optimziation (powered by AI) Software. 
This is part of a DOE project at Oklahoma State University. 

Team memberes:
```
Dr. Geir Hareland
Dr. Runar Nygaard
Dr. Saman Akhtarmanesh
Dr. Mohammed F. Al Dushaishi
Dr. Amin Atashnezhad
```

---

### The Realtime Drilling Optimization Platform has four tabs inclduing:
* Main Page
* Analysis Details
* QC Analysis
* Plot Results

---

### The GUI tabs are seen at the following images.

<p align="left">
  <img width="400" src="Assets/Capture.PNG" >
  <img width="400" src="Assets/Capture2.PNG" >
  <img width="400" src="Assets/Capture3.PNG" >
  <img width="400" src="Assets/Capture4.PNG" >
</p>

---
### Tree structure of Realtime Drilling Optimization Platform is provided at the following.

```
Folder PATH listing for volume OS
Volume serial number is 5448-9438
C:.
|   Function_set.py
|   GUI.ipynb
|   GUI_cleaned_underProgress.ipynb
|   GUI_Functions.py
|   OkstateLogo.ico
|   Part_01.py
|   Part_02.py
|   Part_03.py
|   Plotting.ipynb
|   Plot_function_1.py
|   Plot_function_2.py
|   Plot_function_3.py
|   Plot_function_4.py
|   Plot_function_5.py
|   Plot_function_6.py
|   Plot_function_Vibration.py
|   progress_bar.ipynb
|   QC_function.py
|   README.md
|   Tab_2_Bit_Details.ipynb
|   Tab_2_Bit_Details.py
|   Tab_2_Optimization_Properties.ipynb
|   Tab_2_Optimization_Properties.py
|   Tab_2_PDC_Mud_Heat_Properties_Mud_details.ipynb
|   Tab_2_PDC_Mud_Heat_Properties_Mud_details.py
|   tree.txt
|   Vibration_Analysis.ipynb
|   Vibration_Analysis.py
|   
+---.ipynb_checkpoints
|       GUI-checkpoint.ipynb
|       GUI_cleaned_underProgress-checkpoint.ipynb
|       Plotting-checkpoint.ipynb
|       progress_bar-checkpoint.ipynb
|       Tab_2_Bit_Details-checkpoint.ipynb
|       Tab_2_Optimization_Properties-checkpoint.ipynb
|       Tab_2_PDC_Mud_Heat_Properties_Mud_details-checkpoint.ipynb
|       Vibration_Analysis-checkpoint.ipynb
|       
+---Assets
|       Capture.PNG
|       Capture2.PNG
|       
+---DataSet
|   +---Bit13_Utah_Forge_well_58_32 upper interval
|   |       AI_real_time_opt.csv
|   |       Data_Bit_details.csv
|   |       Data_for_bit_temp.csv
|   |       Data_Operational_Parameters.csv
|   |       Initial_analysis.csv
|   |       Realtime_RS.csv
|   |       
|   +---Bit13_Utah_Forge_well_58_32_lower interval
|   |       AI_real_time_opt.csv
|   |       Data_Bit_details.csv
|   |       Data_for_bit_temp.csv
|   |       Data_Operational_Parameters.csv
|   |       Initial_analysis.csv
|   |       Realtime_RS.csv
|   |       
|   +---Bit1_Chocolate_Mountain_pyspark_cleaned
|   |       Analysis_Details.csv
|   |       Data_Bit_details.csv
|   |       Data_for_bit_temp.csv
|   |       Data_Operational_Parameters.csv
|   |       Initial_analysis.csv
|   |       Realtime_RS.csv
|   |       
|   \---Bit2_Chocolate_Mountain_pyspark_cleaned
|           Data_Bit_details.csv
|           Data_for_bit_temp.csv
|           Data_Operational_Parameters.csv
|           Initial_analysis.csv
|           QC_Data.csv
|           Realtime_RS.csv
|           
+---Figures
|       plot_1.png
|       plot_2.png
|       plot_3.png
|       plot_4.png
|       
+---Images
|       academic-seal.ico
|       academic-seal.jpg
|       Capture.PNG
|       data-analysis-blog.png
|       hnet.com-image (1).ico
|       hnet.com-image.ico
|       OkstateLogo (1).ico
|       OkstateLogo.ico
|       OkstateLogo.png
|       SPE.png
|       
+---Modules
|   |   Bit_Grade.py
|   |   Bit_Grade_With_start.py
|   |   Cutter_Face_Contact_Area.py
|   |   Cutter_Froce.py
|   |   Cutter_Temprature.py
|   |   Cutter_Wear_Flat_Area.py
|   |   Cutter_Work.py
|   |   DE_Algorithm_01.py
|   |   DE_Algorithm_02.py
|   |   DOC_calculation.py
|   |   Drilling_Time_calc.py
|   |   General_Functions.py
|   |   generate_candidate.py
|   |   MSE.py
|   |   Parameters_seperation_functions.py
|   |   Plot_1.py
|   |   Plot_2.py
|   |   Plot_3.py
|   |   Plot_4.py
|   |   ROP_models.py
|   |   Some_necessary_constants.py
|   |   Temprature_models.py
|   |   Time_converter.py
|   |   Wf.py
|   |   
|   +---.ipynb_checkpoints
|   \---__pycache__
|           Bit_Grade.cpython-36.pyc
|           Bit_Grade.cpython-37.pyc
|           Bit_Grade_With_start.cpython-36.pyc
|           Bit_Grade_With_start.cpython-37.pyc
|           Cutter_Face_Contact_Area.cpython-36.pyc
|           Cutter_Face_Contact_Area.cpython-37.pyc
|           Cutter_Froce.cpython-36.pyc
|           Cutter_Froce.cpython-37.pyc
|           Cutter_Temprature.cpython-36.pyc
|           Cutter_Temprature.cpython-37.pyc
|           Cutter_Wear_Flat_Area.cpython-36.pyc
|           Cutter_Wear_Flat_Area.cpython-37.pyc
|           Cutter_Work.cpython-36.pyc
|           Cutter_Work.cpython-37.pyc
|           DE_Algorithm_01.cpython-36.pyc
|           DE_Algorithm_02.cpython-36.pyc
|           DOC_calculation.cpython-36.pyc
|           DOC_calculation.cpython-37.pyc
|           Drilling_Time_calc.cpython-36.pyc
|           General_Functions.cpython-36.pyc
|           General_Functions.cpython-37.pyc
|           generate_candidate.cpython-36.pyc
|           MSE.cpython-36.pyc
|           MSE.cpython-37.pyc
|           Parameters_seperation_functions.cpython-36.pyc
|           Parameters_seperation_functions.cpython-37.pyc
|           Plot_1.cpython-36.pyc
|           Plot_2.cpython-36.pyc
|           Plot_3.cpython-36.pyc
|           Plot_4.cpython-36.pyc
|           ROP_models.cpython-36.pyc
|           ROP_models.cpython-37.pyc
|           Some_necessary_constants.cpython-36.pyc
|           Some_necessary_constants.cpython-37.pyc
|           Temprature_models.cpython-36.pyc
|           Temprature_models.cpython-37.pyc
|           Time_converter.cpython-36.pyc
|           Time_converter.cpython-37.pyc
|           Wf.cpython-36.pyc
|           Wf.cpython-37.pyc
|           
\---__pycache__
        Function_set.cpython-36.pyc
        Function_set.cpython-37.pyc
        GUI_Functions.cpython-36.pyc
        GUI_Functions.cpython-37.pyc
        Parameters_seperation_functions.cpython-36.pyc
        Part_01.cpython-36.pyc
        Part_01.cpython-37.pyc
        Part_02.cpython-36.pyc
        Part_02.cpython-37.pyc
        Part_03.cpython-36.pyc
        Part_03.cpython-37.pyc
        Plot_function_1.cpython-36.pyc
        Plot_function_1.cpython-37.pyc
        Plot_function_2.cpython-36.pyc
        Plot_function_2.cpython-37.pyc
        Plot_function_3.cpython-36.pyc
        Plot_function_3.cpython-37.pyc
        Plot_function_4.cpython-36.pyc
        Plot_function_5.cpython-36.pyc
        Plot_function_6.cpython-36.pyc
        Plot_function_Vibration.cpython-36.pyc
        QC_function.cpython-36.pyc
        ROP_models.cpython-36.pyc
        Some_necessary_constants.cpython-36.pyc
        Tab_2_Bit_Details.cpython-36.pyc
        Tab_2_Optimization_Properties.cpython-36.pyc
        Tab_2_PDC_Mud_Heat_Properties_Mud_details.cpython-36.pyc
        Temprature_models.cpython-36.pyc
        Trunc_function.cpython-36.pyc
        Trunc_function.cpython-37.pyc
        Vibration_Analysis.cpython-36.pyc
        

```



