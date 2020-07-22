import pandas as pd
import numpy as np

df_list = []
def add_column(df,sheet):
    # Empty daaframe
    df1 = pd.DataFrame()
    df1['Plant_Name'] = [sheet.split('_')[-1]]*len(df)

    # Rename column
    df.rename(columns = {'Unnamed: 16':'Plant_Name'}, inplace=True)

    #Replace column
    df = df.assign(Plant_Name=df1['Plant_Name'])
    return df

def date_format(df):
    d = pd.read_excel("FC Model_EAST.xlsx",sheet_name='Summary_RGP',skiprows=1)
    l = []
    for i in d.columns:
        if i[:7] != 'Unnamed':
            l.append(i)
    for i in range(len(df.columns)):
        try:
            a = df.columns[i]
            if a != 'Plant_Name':
                b = l[0] + '_' + df.columns[i].date().strftime("%b-%y")
        except:
            if a[-2:] == '.1':
                if a[:2] == '20':
                    b = l[1] + '_' + pd.to_datetime(a.split('.')[0]).strftime("%b-%y")
                else:
                    b = l[1] + '_' + a.split('.')[0]
            else:
                b = l[0] + '_' + a
        finally:
            if a != 'Plant_Name':
                df.rename(columns = {a:b},inplace=True)
    return df

def main():
    global df_list
    sheets = ['Summary_RGP','Summary_KCW','Summary_BCW','Summary_JCW','Summary_DDSPL']
    # Read from excel
    for sheet in sheets:
        df = pd.read_excel("FC Model_EAST.xlsx",sheet_name=sheet,skiprows=2)

        df = add_column(df,sheet)

        df_list.append(df)

    df = pd.concat(df_list)
    # Replace 0 with NaN
    df.replace(0, np.NaN,inplace=True)
    df = date_format(df)

    # Drop column
    df = df.drop(df.columns[0],axis =1)
    for col in df.columns:
        if col.split('_')[1][:7]=='Unnamed':
            del df[col]


    # Export to excel
    df.to_excel('summary.xlsx',index=False,na_rep='NaN',float_format='%.1f')

if __name__ == "__main__":
    main()
