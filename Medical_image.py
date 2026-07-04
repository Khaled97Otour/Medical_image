import torch 
import cv2 
import numpy as np 
import sklearn
import matplotlib.pyplot as plt
import torch.nn.functional as f 
from skimage.measure import marching_cubes
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import open3d as o3d
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
# testing the modifcation on the code
# other test 

class Brain:
    def __init__(self):
        pass
    def dilation(self, image, kernel = 3): 
        '''
        doing a Morphology operation (dilation) on the input image using the kernel that set to default at 3 
        
        Parameter:
        ----------
        
        image: torch tensor 
            (2D image)
        Kernel: int
            (that is used to determined the size of the kernel (Kernel,Kernel))
        
        Return:
        -------
        2d dilated image the same shape of the input image 
        '''
        
        try:
            image = torch.from_numpy(image)
            return f.max_pool2d(image,kernel_size = kernel ,stride=1 , padding= kernel//2)
        except:
            return f.max_pool2d(image,kernel_size = kernel ,stride=1 , padding= kernel//2)
    def erosion(self, image, kernel = 3):
        '''
        doing a Morphology operation (erosion) on the input image using the kernel that set to default at 3 
        
        Parameter:
        ----------
        
        image: torch tensor 
            (2D image)
        Kernel: int
            (that is used to determined the size of the kernel (Kernel,Kernel))
        
        Return:
        -------
        2d erosion image the same shape of the input image 
        '''
        try:
            image = torch.from_numpy(image)
            return -f.max_pool2d(-image,kernel_size = kernel ,stride=1 , padding= kernel//2)
        except:
            return -f.max_pool2d(-image,kernel_size = kernel ,stride=1 , padding= kernel//2)


    def Opening(self, image, kernel = 3):
        '''
        doing a Morphology operation (Opening) on the input image using the kernel that set to default at 3 
        
        Parameter:
        ----------
        
        image: torch tensor 
            (2D image)
        Kernel: int
            (that is used to determined the size of the kernel (Kernel,Kernel))
        
        Return:
        -------
        2d opened image the same shape of the input image 
        '''
        try:
            image = torch.from_numpy(image)
        except:
            return self.dilation(self.erosion(image, kernel))


    def closing(self, image, kernel = 3):
        '''
        doing a Morphology operation (closing) on the input image using the kernel that set to default at 3 
        
        Parameter:
        ----------
        
        image: torch tensor 
            (2D image)
        Kernel: int
            (that is used to determined the size of the kernel (Kernel,Kernel))
        
        Return:
        -------
        2d Closed image the same shape of the input image 
        '''
        try:
            image = torch.from_numpy(image)
        except:
            return self.erosion(self.dilation(image, kernel))
    
    def read_image(self, path):
        '''
        reading the image from the path         
        Parameter:
        ----------
        
        path: str
            ( the path to the image )
        Return:
        -------
        2d np array image 
        '''
        return cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    
    def Binary_Image(self, image):
        '''
        transform the input image to a binary image          
        Parameter:
        ----------
        
        image: nparray 
            (2D array of the brain image)
        Return:
        -------
        2d np array Binary image 
        '''
        image[image >= 240] = 0
        _, binary_image = cv2.threshold(image, image.mean(), image.max(), cv2.THRESH_BINARY)
        return binary_image
    
    def Display_image(self, image):
        '''
        Display the image          
        Parameter:
        ----------
        image: nparray 
            (2D array of the brain image)
        '''
        cv2.imshow("Display_image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def contour_detecter(self, image):
        '''
        getting the image features and store them in different list          
        Parameter:
        ----------
        
        image: nparray 
            (2D array of the brain image)
        Return:
        -------
        contours: list 
        area: list 
        ratio: list 
        bounding_box: list 
        '''
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print("Number of contours:", len(contours))
        area = []
        ratio = [] 
        bounding_box = []
        for cnt in contours:
            area.append(cv2.contourArea(cnt))
            bounding_box.append(cv2.boundingRect(cnt))
            if cv2.contourArea(cnt) > 50:
                ellipse = cv2.fitEllipse(cnt)
                (center, (major_axis, minor_axis), angle) = ellipse
                ratio.append(major_axis/minor_axis)
            else:
                ratio.append(0)
                continue
            if len(cnt) < 5: 
                ratio.append(0)
                continue

        area = np.asarray(area)
        ratio = np.asarray(ratio)
        print(bounding_box)
        print(area)
        print(area.argsort().argsort())

        print(ratio)
        print(ratio.argsort().argsort())
        return contours , area , ratio , bounding_box

    def Segmentation(self, image):
        '''
        getting the image segmented from the binary image          
        Parameter:
        ----------
        
        image: nparray 
            (2D array of the brain image)
        Return:
        -------
        image_copy: 
            (2d array of the segmented image)
        '''
        counter_image = image.copy()
        contours , area , ratio , bounding_box = self.contour_detecter(image)
        index = 0
        for cnt in contours: 
            if (cv2.contourArea(cnt) > 600) and (ratio[index] > 0.55) and (bounding_box[index][0] > 150) and (bounding_box[index][1] > 140): 
                counter_image = cv2.drawContours(counter_image, contours, index, 255, -1) 
            else: 
                counter_image = cv2.drawContours(counter_image, contours, index, 0, -1) 
            index += 1
    
        if np.count_nonzero(counter_image) == 0:
            counter_image = image.copy()
            index = 0
            for cnt in contours: 
                if (cv2.contourArea(cnt) == area.max()): 
                    counter_image = cv2.drawContours(counter_image, contours, index, 255, -1) 
                else: 
                    counter_image = cv2.drawContours(counter_image, contours, index, 0, -1) 
                index += 1
        index = 0
        for cnt in contours: 
            if (area.max() < 500): 
                counter_image = cv2.drawContours(counter_image, contours, index, 0, -1) 
            index += 1

        image_copy = image.copy()

        image_copy = cv2.bitwise_and(
            image_copy,
            image_copy,
            mask=counter_image
        )
        return image_copy
    def Cluster(self, image):
        '''
        this method get the image into cluster of three which help to analysis the brain image and put it in clusters ( background , gray matter , white matter)       
        Parameter:
        ----------
        image: nparray 
            (2D array of the segmented image)
        Return:
        -------
        images: 
            (threetimes 2d array of the Clustered image)
        '''
        image = cv2.convertScaleAbs(image, alpha=1.7, beta=0)

        cluster = sklearn.cluster.KMeans(n_clusters = 3)
        image_copy_reshaped = image.reshape(-1, 1)

        model = cluster.fit(image_copy_reshaped)
        labels = cluster.labels_

        segmented_image = labels.reshape(image.shape)

        index = np.where(model.cluster_centers_ == model.cluster_centers_.max())

        index1 = np.where(model.cluster_centers_ == model.cluster_centers_.min())

        index2 = np.where((model.cluster_centers_.min() < model.cluster_centers_)&
                        (model.cluster_centers_< model.cluster_centers_.max()))

        label_0 = (segmented_image == index1[0]).astype(np.uint8) * 255

        label_1 = (segmented_image == index2[0]).astype(np.uint8) * 255


        label_3= (segmented_image == index[0]).astype(np.uint8) * 255



        label_0 = cv2.bitwise_and(
            image,
            image,
            mask=label_0
        )



        label_1 = cv2.bitwise_and(
            image,
            image,
            mask=label_1
        )



        label_3 = cv2.bitwise_and(
            image,
            image,
            mask=label_3
        )
        images =[label_0,label_1,label_3]
        return images
    def calculate_mean_variance(self, image_roi):
        """
        Calculates the local mean and variance for each pixel in a region of interest (ROI) 
        using a sliding window, and stores the global mean and variance statistics.

        The function ignores any regions that contain zero values to avoid background 
        or edges that could modify and increase the results. 
        It uses a fixed kernel size (5x5 window) to compute local statistics. Final mean and variance 
        values (excluding zeros) are printed and saved to a global results dictionary using a 
        wavelength/folder-based key.

        Parameters
        ----------
        image_roi : numpy.ndarray
            The input ROI image grayscale, typically masked to exclude irrelevant areas.

        Returns
        -------
        results : dict
            A dictionary with keys as (wavelength, folder) tuples and values containing the rounded
            mean, standard deviation, and variance of the pixel intensities.

        Notes
        -----
        - Uses global variables: `folder`, `match`, and `results`.
        - Kernel size is fixed at 5x5.
        - Pixels with any zero in their neighborhood window are skipped.
        - Results are  stored in a global `results` dictionary.
        """
        pixel_vars = []
        pixel_means = []
        mean = [] 
        variance = []
        kernel_size = 5  # (3+2) on each side
        pad_size = kernel_size // 2

        # Pad the image to avoid boundary issues
        #padded_image = np.pad(image_roi, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='constant', constant_values=0)
        for x in range(image_roi.shape[0]):
            for y in range(image_roi.shape[1]):
                # Extract the region of interest (ROI)
                current_roi = image_roi[x:x + kernel_size, y:y + kernel_size]

                # Skip if any zero values are present
                if np.any(current_roi == 0):
                    continue

                # Compute mean and variance
                pixel_mean = np.mean(current_roi)
                pixel_var = np.var(current_roi)

                pixel_means.append(pixel_mean)
                pixel_vars.append(pixel_var)

        # Convert lists to NumPy arrays
        if pixel_means:
            pixel_mean_np = np.array(pixel_means)
            pixel_vars_np = np.array(pixel_vars)
        else: 
            pixel_mean_np = np.array([]) 
            pixel_vars_np = np.array([])
        # Compute final statistics excluding zeros
        if pixel_mean_np.size > 0 and np.any(pixel_mean_np != 0):
            mean.append(np.mean(pixel_mean_np[pixel_mean_np != 0]))
            variance.append(np.var(pixel_mean_np[pixel_mean_np != 0]))
        else:
            mean.append(0)
            variance.append(0)
        total_mean_value = np.mean(mean)
        total_variance_value = np.mean(variance) 

        return round(total_mean_value,4) , round(total_variance_value,4)
    def plot_the_measurement(self, images):
        Mean = []
        Variance = []

        for image in images:
            mean , variance = self.calculate_mean_variance(image)
            Mean.append(mean)
            Variance.append(variance)

        Titles = ['Background', 'gray matter', 'white matter']

        plt.subplot(1, 2, 1)
        plt.scatter(Titles,Mean)
        plt.xlabel('area')
        plt.ylabel('Mean')

        plt.subplot(1, 2, 2)
        plt.scatter(Titles,Variance)
        plt.xlabel('area')
        plt.ylabel('Variance')

        plt.show()
    def get_segmented_image(self, path):
        Image = self.read_image(path)
        binary_image = self.Binary_Image(Image)
        kernel = np.ones((3,3), np.uint8)
        open_image = cv2.morphologyEx(binary_image,cv2.MORPH_OPEN,kernel, iterations=2)
        segmented_image = self.Segmentation(open_image)
        Image = cv2.bitwise_and(
            Image,
            Image,
            mask=segmented_image
        )
        return Image
    
    def get_Clustered_image(self, path):
        image  = self.get_segmented_image(path)
        return self.Cluster(image)
        
    def Display_Clustered_image(self, image):
        index = 0
        for img in image: 
            cv2.imshow(f"segmente image {index}",img)
            index +=1

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def Display_3D_Model(self, root_path, flag = 1):
        Images = []
        for file_name in sorted(os.listdir(root_path)):
            file_path = os.path.join(root_path, file_name)
            try:
                if flag == 0:
                    img = Brain.read_image(file_path)
                if flag == 1:
                    img = Brain.get_segmented_image(file_path)
                Images.append(img)
            except:
                continue
        volume = np.stack(Images, axis=0).astype(float)
        
        points = []
        for z in range(volume.shape[0]):
            y, x = np.where(volume[z] > 0)
            for i in range(len(x)):
                points.append([x[i], y[i], z])
        points = np.array(points)
        verts, faces, normals, values = marching_cubes(
            volume,
            level=0.001
        )
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)

        o3d.visualization.draw_geometries([pcd])

Brain = Brain()
# hide main tkinter window
file_path = None
root_path = None

while(1):
    feature = input("Select your process: 'img' for one image 'folder' for a sequence of images ")
    
    if feature == 'img':
        Tk().withdraw()
        file_path = askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
                ("All Files", "*.*")
            ]
        )
        break
    if feature == 'folder':
        Tk().withdraw()

        root_path = askdirectory(title="Select Folder that has the sequence of the images")
        break
    else:
        print("wrong input try again")
        
if file_path != None:
    while(1):
        feature = input("Select your process: 'img' to just display image, 'seg' for a segmented Images, 'cluster' for divide the image into clusters ")
        if feature == 'img':
            image = Brain.read_image(file_path)
            Brain.Display_image(image)
            break
        if feature == 'seg':
            segmented_Images = Brain.get_segmented_image(file_path)
            Brain.Display_image(segmented_Images)
            break
        if feature == 'cluster':
            Images = Brain.get_Clustered_image(file_path)
            Brain.Display_Clustered_image(Images)
            Brain.plot_the_measurement(Images)
            break
        else:
            print("wrong input try again")
if root_path != None:
    while(1):
        feature = input("Select the method just the image '0' or the segmented images '1' ")
        if feature == '0' or  feature == '1':
            Brain.Display_3D_Model(root_path,int(feature))
            break
        else: 
            print("wrong input try again")