# Soil erosion detection
This problem is a part of Quantum test task. Other problems can be found at the [main repo](https://github.com/nktntp/quantum-test-task).

## Project Objective
Given a raster dataset and a mask file train a model to classify if there is an erosion of a field.

## Technologies
- Python3
- Rasterio
- GeoPandas
- TensorFlow
- Keras
- Numpy
- Pandas
  
## Project Description
### Data Preparation
Each field from __.shp__ file was cutted from a map. For this purpose, Rasterio has a function called __mask__.

``` Python
for num, row in train_df.iterrows():
    try:
      masked_image, out_transform = rasterio.mask.mask(src, [mapping(row['geometry'])], crop=True, nodata=0)
      img_image = reshape_as_image(masked_image)        
      img_path = os.path.join(outfolder, str(num) + '.png')
      img_image = cv2.cvtColor(img_image, cv2.COLOR_RGB2BGR)
      cv2.imwrite(img_path, img_image)
      
    except Exception as e:
      failed.append(num)
print("Rasterio failed to mask {} files".format(len(failed)))
```
Rasterio failed to mask 435 files from 936.

Since only 334 had corresponding description the images were labled manually into two categories 1: "Normal" and 2: "Erosion".
### Model Training

Classification task was solved with the help of transfer learning. __InceptionV3__ with weights in feature generation layers pretrinated on imagenet was chosen as the model.

Optimizer - Adam

Loss function - Categorical Crossentropy

#### Training results

<p float="left">
  <img src="https://github.com/nktntp/quantum-test-task/blob/master/task4/img/loss.png" width="300" />
  <img src="https://github.com/nktntp/quantum-test-task/blob/master/task4/img/accuracy.png" width="300" />
</p>

