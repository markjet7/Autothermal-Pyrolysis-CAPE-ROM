# This code is a function that predicts the pyrolysis yields based on the feedstock composition 
def pyrolysis(feedstock_comp):
    import pandas as pd
    import pickle
    
    
# The next line imports the ranzi data to extract the products 
    products = ['CELLA','HCEA1','HCEA2','LIG','LIGCC','LIGOH','GCO2','GCO','GCOH2','GH2','Char','HAA','GLYOX','C3H6O','C3H4O2','HMFU','LVG', 'XYL','pCOUMARYL','PHENOL','FE2MACR','CH3CHO','ETOH','CH3OH','CO','CO2','CH4','CH2O','H2','C2H4','H2O']
    molar_mass = np.array([0.162,0.132,0.132,0.208,0.258,0.378,0.044,0.028,0.03,0.002,0.012,0.06,0.058,0.058,0.072,0.126,0.162,0.132,0.15,0.094,0.208,0.044,0.046,0.032,0.028,0.044,0.016,0.03,0.002,0.028,0.018])
    
    # The next line creates an empty list, the products predicted are going to be stored in this list while we loop through each product model    
    predictions =[]

# The for loop will loop through the products models that was trained and saved earlier, predict and append each product to the prediction list 
    for index,name in enumerate (products):
        model = 'model' + name + ".sav"
        model2 = pickle.load(open(model,'rb'))
        pred = model2.predict(feedstock_comp)         
        prod_mol = pred/molar_mass[index]
        
        predictions.append(pred_mol)
    return (predictions)

