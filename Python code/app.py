from flask import Flask,redirect,url_for,render_template,request
import pickle
import numpy as np
import requests
import os
from skimage.io import imread
from skimage.transform import resize

crop_recommendation_model_path = '../models/crop_recommend.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))

apple_disease_model_path = '../models/apple.pkl'
apple_disease_model = pickle.load(open(apple_disease_model_path, 'rb'))

cherry_disease_model_path = '../models/cherry.pkl'
cherry_disease_model = pickle.load(open(cherry_disease_model_path, 'rb'))

grape_disease_model_path = '../models/grape.pkl'
grape_disease_model = pickle.load(open(grape_disease_model_path, 'rb'))

maize_disease_model_path = '../models/maize.pkl'
maize_disease_model = pickle.load(open(maize_disease_model_path, 'rb'))

tomato_disease_model_path = '../models/tomato.pkl'
tomato_disease_model = pickle.load(open(tomato_disease_model_path, 'rb'))

potato_disease_model_path = '../models/potato.pkl'
potato_disease_model = pickle.load(open(potato_disease_model_path, 'rb'))

crop_yeild_model_path = '../models/cropyeild.pkl'
crop_yeild_model = pickle.load(open(crop_yeild_model_path, 'rb'))


app=Flask(__name__)

@app.route('/')
def welcome():
    
    return render_template('homepage.html')


@ app.route('/crop_prediction')
def crop_prediction():
    title = 'Kisaan help desk - crop recommendation'
    return render_template('cropprediction.html', title=title)



@app.route('/fertilizer_rec')
def fertilizer_rec():
    title = 'Kisaan help desk - fertilizer recommendation'
    return render_template('fertilizerrecommendation.html', title=title)

@app.route('/soil_test')
def soil_test():
    title = 'Kisaan help desk - soil test'
    return render_template('soiltest.html', title=title)

@app.route('/crop_disease')
def crop_disease():
    title = 'Kisaan help desk - crop disease prediction'
    return render_template('cropdisease.html', title=title)

@app.route('/crop_yeild')
def crop_yeild():
    title = 'Kisaan help desk - crop yeild prediction'
    return render_template('cropyeild.html', title=title)


@app.route('/submit2',methods=['POST','GET'])
def Submit2():
    if request.method=='POST':
        state=(request.form['state'])
        
        if state!=None:
            if state=='andhrapradesh':
                return render_template('Andhrapradesh.html')
            if state=='arunachalpradesh':
                return render_template('Arunachalpradesh.html')
            if state=='assam':
                return render_template('Assam.html')
            if state=='bihar':
                return render_template('Bihar.html')
            if state=='chandigarh':
                return render_template('Chandigarh.html')
            if state=='chattisgarh':
                return render_template('Chattisgarh.html')
            if state=='delhi':
                return render_template('Delhi.html')
            if state=='gujarat':
                return render_template('Gujarat.html')
            if state=='haryana':
                return render_template('Haryana.html')
            if state=='himachalpradesh':
                return render_template('Himachalpradesh.html')        
            if state=='jammuandkashmir':
                return render_template('Jammuandkashmir.html')
            if state=='jharkhand':
                return render_template('Jharkhand.html')
            if state=='karnataka':
                return render_template('Karnataka.html')
            if state=='kerala':
                return render_template('Kerala.html')
            if state=='madyapradesh':
                return render_template('Madyapradesh.html')
            if state=='maharastra':
                return render_template('Maharastra.html')
            if state=='manipur':
                return render_template('Manipur.html')
            if state=='meghalaya':
                return render_template('Meghalaya.html')
            if state=='mizoram':
                return render_template('Mizoram.html')
            if state=='orissa':
                return render_template('Orissa.html')
            if state=='punjab':
                return render_template('Punjab.html') 
            if state=='rajasthan':
                return render_template('Rajasthan.html') 
            if state=='sikkim':
                return render_template('Sikkim.html') 
            if state=='tamilnadu':
                return render_template('Tamilnadu.html') 
            if state=='telangana':
                return render_template('telangana.html') 
            if state=='uttarkhand':
                return render_template('Uttarkhand.html')
            if state=='uttarpradesh':
                return render_template('Uttarpradesh.html')
            if state=='westbengal':
                return render_template('Westbengal.html')  
            else:
                return render_template('tryagain.html')                                                              


@app.route('/submit',methods=['POST','GET'])
def submit():
    my_prediction=0
    if request.method=='POST':
        N=int(request.form['N'])
        P=int(request.form['P'])
        K=int(request.form['K'])
        temperature=float(request.form['temperature'])
        humidity=float(request.form['humidity'])
        ph= float(request.form['ph'])
        rainfall=float(request.form['rainfall'])
        if ph != None:
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]
            return render_template('cropres.html', result=final_prediction)
        else:
            return render_template('tryagain.html')


@app.route('/submit1',methods=['POST','GET'])
def submit1():
    if request.method=='POST':
        N=int(request.form['N'])
        P=int(request.form['P'])
        K=int(request.form['K'])
        if N>=45 and P>=50 and K>=80:
            return render_template('NPKhigh.html')
        elif N<=35 and P<=30 and K<=40:
            return render_template('NPKlow.html')    
        elif N>=45 and P>=50 and K<=80:
            return render_template('NPhigh.html')
        elif N>=45 and P<=50 and K>=80:
             return render_template('NKhigh.html')
        elif N<=45 and P>=50 and K>=80:
             return render_template('PKhigh.html')
        elif N>=45 and P<=50 and K<=80:
             return render_template('Nhigh.html')
        elif N<=45 and P>=50 and K<=80:
            return render_template('Phigh.html')
        elif N<=45 and P<=50 and K>=80:
             return render_template('Khigh.html')
        elif N<=35 and P<=30 and K>=39:
             return render_template('NPlow.html')
        elif N>=35 and P<=30 and K<=39:
             return render_template('PKlow.html')
        elif N<=35 and P>=30 and K<=39:
             return render_template('NKlow.html')                                  
        elif N<=35 and P>=30 and K>=39:
             return render_template('Nlow.html')
        elif N>=35 and P<=30 and K>=39:
             return render_template('Plow.html')
        elif N>=35 and P>=30 and K<=39:
             return render_template('Klow.html')
        elif N>=35 and N<=45 and P>=30 and P<=50 and K>=39 and K<=80:
            return render_template('NPKok.html') 
                          
@app.route('/submit3',methods=['POST','GET'])
def submit3():
    if request.method=='POST':
        x= request.form["Crop"]
        if (x == 'Arhar'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=1,0,0,0,0,0,0,0,0,0
        if (x == 'Cotton'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,1,0,0,0,0,0,0,0,0
        if (x == 'Gram'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,1,0,0,0,0,0,0,0
        if (x == 'Groundnut'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,1,0,0,0,0,0,0
        if (x == 'Maize'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,1,0,0,0,0,0
        if (x == 'Moong'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,1,0,0,0,0
        if (x == 'Paddy'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,1,0,0,0
        if (x == 'RM'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,0,1,0,0
        if (x == 'Sugarcane'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,0,0,1,0
        if (x == 'Wheat'):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,0,0,0,1
        
        y= request.form["State"]
        if (y == 'AP'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=1,0,0,0,0,0,0,0,0,0,0,0,0
        if (y == 'Gujarat'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,1,0,0,0,0,0,0,0,0,0,0,0
        if (y == 'Karnataka'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,1,0,0,0,0,0,0,0,0,0,0
        if (y == 'Maharashtra'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,1,0,0,0,0,0,0,0,0,0
        if (y == 'UP'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,1,0,0,0,0,0,0,0,0
        if (y == 'Haryana'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,1,0,0,0,0,0,0,0
        if (y == 'Punjab'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,1,0,0,0,0,0,0
        if (y == 'MP '):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,1,0,0,0,0,0
        if (y == 'Rajasthan'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,0,1,0,0,0,0
        if (y == 'TN'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,0,0,1,0,0,0
        if (y == 'Bihar'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,0,0,0,1,0,0
        if (y == 'Orissa'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,0,0,0,0,1,0
        if (y == 'WB'):
            y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=0,0,0,0,0,0,0,0,0,0,0,0,1
        print(x)
        print(y)
        a= request.form["cost"]
        print(a)
        b= request.form["cost1"]
        print(b)
        c= request.form["cost2"]
        print(c)
        d= request.form["price"]
        print(d)
        
        input_val=[[int(x0),int(x1),int(x2),int(x3),int(x4),int(x5),int(x6),int(x7),int(x8),int(x9),int(y0),int(y1),int(y2),int(y3),int(y4),int(y5),int(y6),int(y7),int(y8),int(y9),int(y10),int(y11),int(y12),float(a),float(b),float(c),float(d)]]        
        pred = crop_yeild_model.predict(input_val)
        print(pred[0])
        return render_template("cropyeildresult.html", text = pred[0])
            
        '''Land=float(request.form['Land'])
        print(Land)        price=int(request.form['price'])
        print(price)
        Crop=(request.form['Crop'])
        print(Crop)
        if Land!=None and price!=None and Crop!=None:
            if Crop=='Apple':
                yeild=Land*25
                money=price*yeild
                return render_template('cropyeildres.html',result1=yeild,result2=money)'''




@app.route('/submit4',methods=['POST','GET'])
def submit4():
    my_prediction=0
    if request.method=='POST':
        crop=(request.form['Crop'])
        file=(request.files['file'])
        if crop == 'Apple' :
                CATAGORIES=['Apple_scab','Black_rot','Cedar_apple_rust']
                flat_data=[]
                url=(file)
                img=imread(url,pilmode="RGB")
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape)
                pred=apple_disease_model.predict(flat_data)
                print(pred)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]
                return render_template('cropdiseaseres.html', result=y_out)
        if crop == 'Cherry' :
                CATAGORIES=['cherry_healthy','cherry_powdery_mildew']
                flat_data=[]
                url=(file)
                img=imread(url)
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape)
                pred=cherry_disease_model.predict(flat_data)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]               
                return render_template('cropdiseaseres.html', result=y_out) 
        if crop == 'Grape' :
                CATAGORIES=['black_rot','esca','healthy','leaf_blight']
                flat_data=[]
                url=(file)
                img=imread(url)
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape)
                pred=grape_disease_model.predict(flat_data)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]
                return render_template('cropdiseaseres.html', result=y_out)
        if crop == 'Maize' :
                CATAGORIES=['Northern_leaf_blight','cercospora_leaf_spot','common_rust','healthy']
                flat_data=[]
                url=(file)
                img=imread(url)
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape) 
                pred=maize_disease_model.predict(flat_data)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]
                return render_template('cropdiseaseres.html', result=y_out)  
        if crop == 'Potato' :
                CATAGORIES=['potato_early_blight','potato_healthy','potato_late_blight']
                flat_data=[]
                url=(file)
                img=imread(url)
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape) 
                pred=potato_disease_model.predict(flat_data)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]
                return render_template('cropdiseaseres.html', result=y_out)     
        if crop == 'Tomato' :
                CATAGORIES=['tomato_early_blight','tomato_healthy','tomato_late_blight']
                flat_data=[]
                url=(file)
                img=imread(url)
                img_resized=resize(img,(150,150,3))
                flat_data.append(img_resized.flatten())
                flat_data=np.array(flat_data)
                print(img.shape) 
                pred=potato_disease_model.predict(flat_data)
                l=np.amax(pred)
                l   
                f=pred.astype(int)
                f
                a1=np.array(f)
                print(a1)
                from functools import reduce
                single_list = reduce(lambda x,y: x+y, a1)
                print(single_list)
                '''val=np.where(single_list==1)
                dou_list = reduce(lambda x,y: x+y, val)
                print(dou_list)
                stringed = ''.join(map(str,val))
                stringed
                v=stringed[1]
                v1= int(v)
                v1'''
                y_out=CATAGORIES[single_list]
                return render_template('cropdiseaseres.html', result=y_out)                                           
            


            



if __name__=='__main__':
    app.run(debug=False)