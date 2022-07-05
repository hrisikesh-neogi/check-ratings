import pandas as pd
import os
import warnings

warnings

def delete_unrated_chat_ratings():
    file = os.listdir('uploads')[0]
    data = pd.read_excel('uploads/'+file, skiprows=2)
    
    #lets create a new copy of the existing dataset
    df = data.copy()

    #if not rated, feedback is '-', so' lets delete
    for row in df.index:
        rating = df['Feedback'][row]
        if rating == '-':
            df = df.drop(row)
    return df
        




def check_rating(rating = 'all_', name=None):

    df = delete_unrated_chat_ratings()


    df['Feedback'] = df['Feedback'].astype(int)
    # print( df['Feedback'].unique() )

    #if name is not None
    if name == None:
        final = df[df['Feedback'] == rating]
    else:
        df['Agent'] = df['Agent'].apply(lambda x: x.strip())
        final = df[df['Agent'] == name]
        if rating != 'all_':
            final = final[final['Feedback'] == rating]
        
            


    final = final[['Agent', 'Feedback']]
    final = final.reset_index(drop=True)
    return final
    # print(df.columns)


# dd = check_rating(name = 'Hrisikesh', rating=5)
# print(dd)