# Project descriptions
     1.Rock vs mine prediction:
           - this model using 'logistic regression' predicts whether readings of sonar are for mine or rock.


           
     2.Spam mail prediction:
           - we perform feature extraction data using Tfidf vectorizer to remove stop words,
           the data then is used to train model on 'logistic regression',which predicts if given
           mail is spam or ham.


           
     3.Wine Quality Prediction
           - model is trained using 'random forest classifier' to predict the quality of wine
           - only wine with quality > 7 qualifies as good quality wine hence its label is '1' 
           whereas for wine with quality < 7 is not a great qualtiy rating hence its label is '0'.


           
     4.Parkinsons disease prediction
           - standardized data is used to train model which uses 'SVC' to predict if the person has 
           parkinsons disease or not.


           
     5.Movie recommendation system
           - various features are combined together,which are then assigned weights using TFidf vectorizer
           - 'cosine similarity' function is used to find closest vectors to input vectors and then the output
           is displayed.


           
     6.Loan status prediction
           - data is processed and encoded,which is then use to train model which uses 'SVC' to approve or reject loan.


     
     7.House price prediction
           - model uses 'XGB regressor' to predict the price of house.


     
     8.Heart disease prediction
           - 'Logistic regrssion model' is trained to tell the condition of heart.


     
     9.Fake news prediction
           - data is first processed where words that have less weight(stopwords) are removed from feature attributes.
           - the features are then vectorized and 'logistic regression' model is trained on this processed data to classify
           news as fake or real.



     10.Diabetes prediction
           - data is standardized to improve model's training.
           - 'SVC' model is used to predict whether person is diabetic or not.


     
     11.Customer Segmentation
           - standardized data is used to train 'kMeans' model to assign clusters to customer based on their purchases.


     
     12.Calories Burnt prediction
           - 'XGB regressor' model is trained on data to predict the amount of calories burnt based on feature attributes.


     
     13.Breast cancer classification
           - 'Logistic regression' model is trained to classify type of breast cancer based on patients report data.


     
     14.Big mart sales prediction
           - data is processed and visualized to determine feature attributes.
           - this processed data is then used to train 'XGB regressor' model to predict sales of a outlet.
