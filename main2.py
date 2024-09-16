import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import json

#Tensorflow Model Prediction
def model_prediction(image_path, target_size=(225, 225)):
   

    img = load_img(image_path, target_size=target_size)
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    return np.argmax(predictions)
    

#Sidebar
st.sidebar.title("FARM CREW")
app_mode = st.sidebar.selectbox("view Features",["Home","Disease Detection","Smart Fertilizer","Multicroping Methods","About"])

#Main Page
if(app_mode=="Home"):
    
            st.markdown("""
                        <style>
                        .home{
                            color:#16423C;
                            font-size:40px;
                            font-style:italic;
                            font-weight:bold;
                            width:100%;
                            text-align:center;
                            margin-bottom:60px;
                            
                            border-radius:20px;
                            }
                
                </style>
                <style>
                        .home1{
                            color:#16423C;
                            font-size:40px;
                            font-style:italic;
                            font-weight:bold;
                            width:100%;
                            text-align:left;
                            margin-bottom:20px;
                            
                            border-radius:20px;
                            }
                
                </style>
                <style>
                .para-1{
                    color:#063970;
                    font-size:24px;
                    text-align:center;
                    margin-bottom:20px;
                    padding:5px;
                }
                </style>
                <style>
                   .img{
                       width:100%;
                       border-radius:20px;
                       text-align:center;
                       height:380px;
                       box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
                       margin-bottom:30px;
                       
                       
                   }
                   
                </style>
                <style>
                   .card-1{
                       margin-bottom:30px;
                           
                       
                   }
                </style>
                <style>
                     .head-1{
                         color:#16423C;
                        font-size:26px;
                        font-style:italic;
                        font-weight:bold;
                        width:100%;
                        text-align:left;
                        
                        margin-bottom:20px;
                        margin-left:20px;
                        
                       
                     }
                </style>
                <style>
                   .img1{
                       width:80%;
                       border-radius:20px;
                       text-align:center;
                       height:300px;
                       box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
                       margin-bottom:30px;
                       margin-left:20px;
                       
                </style>
                <style>
                   .para-2{
                    color:#063970;
                    font-size:24px;
                    text-align:left;
                    margin-bottom:20px;
                    padding:5px;
                }
                </style>
                <style>
                  .list-1{
                    color:#063970;
                    font-size:22px;
                    text-align:left;
                    margin-bottom:20px;
                    padding:5px;
                }
                  
                </style>
                 <style>
                    .button {
                        display: inline-block;
                        padding: 10px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #007bff;
                        border: none;
                        border-radius: 5px;
                        text-align: center;
                        cursor: pointer;
                        text-decoration: none;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        transition: all 0.3s ease;
                        margin:;
                        
                    }

                    .button:hover {
                        background-color: #0056b3;
                        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
                        transform: translateY(-3px);
                    }
                  </style>
                  <style>
                      .flex-container {
                            display: flex;
                            justify-content: center; /* Center horizontally */
                            align-items: center; /* Center vertically */
                            height: 100px; /* Set a height for vertical centering */
                        }
                  </style>
                  <style>
                     .card-2{
                         margin-bottm:40px;
                     }
                  </style>
                
                
                <div class="card-1">
                <div>
                 <h1 class="home">AI-Powered Crop Disease Detection and Management</h1>
                <img src="https://res.cloudinary.com/dnc8iinjd/image/upload/v1726484980/Colorful_Modern_Brand_Identity_Flow_Chart_enznve.png" class="img"/>
               
                <p class="para-1">At Farm Crew, we are transforming agriculture with the power of AI. Our platform offers farmers an innovative solution to detect crop diseases early and take timely preventive actions. By utilizing state-of-the-art machine learning algorithms and real-time environmental data, Farm Crew accurately identifies crop diseases from images, predicts potential outbreaks, and provides tailored treatment recommendations.</p>
                <p class="para-1">Accessible via both web and mobile platforms, Farm Crew helps farmers enhance productivity, minimize losses, and maintain healthier crops. Join us in advancing sustainable farming with Farm Crew – your trusted ally in smart agriculture.</p>
                <div class="flex-container"> <a style="color:black;" class="button" >Explore Now!</a></div>
                </div>
                </div>
                
                
                <div>
                   <h1 class="home1">Explore Our Advanced Features</h1>
                   <div class="card-2">
                     <h1 class="head-1">SMART FERTILIZER</h1>
                     <img src="https://res.cloudinary.com/dnc8iinjd/image/upload/v1726478953/Designer_3_qu2hld.png" class="img1"/>
                     <p class="para-2">Our Smart Fertilizer Recommendation system is designed to revolutionize how you manage soil nutrients and enhance crop growth. Using advanced AI algorithms and real-time data, our system delivers tailored fertilizer recommendations that are both efficient and effective, ensuring your crops receive exactly what they need to thrive.</p>
                     <ul class="list-1">
                        <li>Data-Driven Insights: Our system leverages comprehensive soil analysis, weather conditions, and crop growth data to provide precise fertilizer recommendations. By understanding the specific needs of your soil and plants, we help you apply the right nutrients at the right time.</li>
                        <li>Real-Time Adjustments: Benefit from real-time updates and adjustments based on changing environmental conditions and plant growth stages. Our system continuously monitors data and adjusts recommendations to optimize nutrient uptake and minimize waste.</li>
                        <li>Customizable Plans: Tailor your fertilization strategy to different crop types and growth phases. Whether you’re growing vegetables, grains, or fruits, our Smart Fertilizer system delivers customized recommendations to support optimal growth and yield.</li>
                        <li>Environmental Impact Reduction: By using targeted recommendations, our system helps reduce over-application of fertilizers, minimizing runoff and environmental impact. This approach promotes sustainable farming practices and enhances soil health over time.</li>
                        <li>User-Friendly Interface: Access detailed recommendations and track your fertilization plans through an intuitive, easy-to-use interface. Our platform provides actionable insights and guides you through the application process, ensuring you make the most informed decisions for your crops.</li>
                        <div class="flex-container"><a style="color:black;" class="button" >Use Me!</a></div>
                     </ul>
                   </div>
                   <div>
                     <h1 class="head-1">SMART FERTILIZER</h1>
                    <img src="https://res.cloudinary.com/dnc8iinjd/image/upload/v1726482093/Designer_2_ckblyt.png" class="img1"/>
                    <p class="para-2">Our AI-powered multi-cropping recommendation system leverages data science to help farmers choose the best crop combinations based on factors such as soil health, climate conditions, and market demand. Here's how it works</p>
                     <ul class="list-1">
                        <li>Multi-cropping enhances soil fertility by reducing nutrient depletion. Different crops utilize different nutrients, helping maintain soil balance and structure.</li>
                        <li>By planting multiple crops on the same land, farmers can maximize their land use, increasing productivity per acre.</li>
                        <li>Diverse crop environments disrupt pest life cycles and make it harder for diseases to spread, reducing the need for chemical pesticides.</li>
                        <li>Encourages the cultivation of a variety of crops, which supports biodiversity and creates a more resilient agricultural ecosystem.</li>
                        <li>Crops that complement each other can result in higher yields than when grown individually, providing a boost in overall farm productivity.</li>
                        <div class="flex-container"><a style="color:black;" class="button" >Use Me!</a></div>
                     </ul>
                   </div>
                </div>
                <div>
                   <h1 class="home1">Work Flow of AI-Model<h1>
                    <video width="640" height="360" controls autoplay muted loop poster="thumbnail.jpg" preload="auto">
                    <source src="https://res.cloudinary.com/dnc8iinjd/video/upload/v1726483005/client_1_a7pyci.mp4" type="video/mp4">
                    <source src="movie.ogv" type="video/ogg">
                    Your browser does not support the video tag.
                    </video>

                <div>
                
            
            """,unsafe_allow_html=True)
   

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)

#Prediction Page
elif(app_mode=="Disease Detection"):
    st.header("Disease Recognition")
    st.markdown("""
                <style>
                    .img{
                       width:100%;
                       border-radius:20px;
                       text-align:center;
                       height:380px;
                       box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
                       margin-bottom:80px;
                       margin-top:40px;
                       
                       
                   }
                   
                </style>
                <div>
                   <img src="https://res.cloudinary.com/dnc8iinjd/image/upload/v1726486164/Violet_and_Gray_Hexagon_Process_Diagram_wfkdrj.png" class="img"/>
                </div>
                """,unsafe_allow_html=True)
    
    
    image_path=st.file_uploader("Uplaod_photo: ")
       
        
    
    
    if(st.button("Show Image")):
        st.image(image_path,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        model = load_model('model.h5')
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(image_path, target_size=(225, 225))
        #Reading Labels
        lables={0:"Healthy",1:"Powdery",2:"Rust"}
        
        
        
        if result_index==0:
            st.markdown("""
                        <style>
                           .home2{
                            color:#16423C;
                            font-size:36px;
                            font-style:italic;
                            
                            width:100%;
                            text-align:left;
                            margin-bottom:20px;
                            margin-left:20px;
                            border-radius:20px;
                            
                            }
                        </style>
                        <style>
                            .para-1{
                                color:#063970;
                                font-size:24px;
                                text-align:left;
                                margin-bottom:20px;
                                padding:5px;
                                margin-left:20px;
                            }
                        </style>
                        <div>
                          <h1 class="home2">Your Crop is in Good condition</h1>
                          <p class="para-1">You can use Our Advanced Feautres</p>
                        <div>
                        """,unsafe_allow_html=True)
            if st.button("SMART FERTILIZER"):
                 st.success("Sorry we implement this in future Rounds {}")
            elif st.button("MULTI CROPPING METHODS"):
                st.success("Sorry we implement this in future Rounds {}")     
     
            
        else:
                  
           st.markdown("""
                        <style>
                           .home2{
                            color:#16423C;
                            font-size:36px;
                            font-style:italic;
                            font-weight:bold;
                            width:100%;
                            text-align:left;
                            margin-bottom:20px;
                            margin-left:20px;
                            border-radius:20px;
                            }
                        </style>
                        <div>
                          <h1 class="home2">Your Crop is in Bad condition</h1>
                        <div>
                        """,unsafe_allow_html=True)
        
        
elif(app_mode=="Smart Fertilizer"):
    st.header("Sorry we implement this in future Rounds") 
elif(app_mode=="Multicroping Methods"):
   st.header("Sorry we implement this in future Rounds")    
  
    
         
        
