# OpenCVExercises

1. Programs will firstly read the rows and then read the cols and last read the type. The order of pixel structure is bit_depth, then colorspaces, and then number_of_channel.


2. For the RGB outputs, the red output only keeps the value of red, so does the green and blue output. In the red picture, the nose part is    very light while in blue picture, the part beside nose is very bright since this part is blue in the original pictrue.

   Y shows the luminance, Cb shows how blue these pixels are, and Cr shows how red these pixels are. In Cr picture, the nose part is very      dark while in Cb pictrue, the nose part is very light. 
   
   In Hue pictrue, the nose part is much darker than the part beside the nose, it is because in Hue pictrues, when color is red, the value    is small. And Value picture means how bright each parts of picture is. And Saturation picture means how pure a color is, so the nose        part is very bright other than other part.
   
   For RGB, the value is 102, 165, 156. They all range from 0-255.
   For YCrCb, the value is 155, 129, 98. Y ranges from 0-255, Cb,Cr range from 16-255.
   For hsv, the value is 34, 97, 165. H ranges from 0-360, S and V range from 0-100.
  
3. When pictures are added with GaussianNoise, the Gaussian Filter works better. And when pictures are added with Salt&Pepper Noise, the Median Filter works better.
