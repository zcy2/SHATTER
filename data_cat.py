import pandas as pd
network_data = ['network_scalefree_90-150','network_scalefree_150-300','network_scalefree_300-600','network_scalefree_600-900','network_random_90-150','network_random_150-300','network_random_300-600','network_random_600-900','network_smallworld_90-150','network_smallworld_150-300','network_smallworld_300-600','network_smallworld_600-900']
for net_data in network_data:
    col_name = ['N', 'ID', 'ANOC']

    #SHATTER
    df_SHATTER = pd.read_csv('./save/'+net_data+'/SHATTER/reward.csv')
    df_SHATTER.columns = col_name
    df_SHATTER = df_SHATTER.drop(columns=['N', 'ID'])
    df_SHATTER.insert(1, 'Algorithms', 'SHATTER')

    #HDA
    df_HDA = pd.read_csv('./save/'+net_data+'/HDA/reward.csv')
    df_HDA.columns = col_name
    df_HDA = df_HDA.drop(columns=['N', 'ID'])
    df_HDA.insert(1, 'Algorithms', 'HDA')

    #HPA
    df_HPA = pd.read_csv('./save/' + net_data + '/HPA/reward.csv')
    df_HPA.columns = col_name
    df_HPA = df_HPA.drop(columns=['N', 'ID'])
    df_HPA.insert(1, 'Algorithms', 'HPA')

    # HDSA
    df_HDSA = pd.read_csv('./save/' + net_data + '/HDSA/reward.csv')
    df_HDSA.columns = col_name
    df_HDSA = df_HDSA.drop(columns=['N', 'ID'])
    df_HDSA.insert(1, 'Algorithms', 'HDSA')

    # HDDA
    df_HDDA = pd.read_csv('./save/' + net_data + '/HDDA/reward.csv')
    df_HDDA.columns = col_name
    df_HDDA = df_HDDA.drop(columns=['N', 'ID'])
    df_HDDA.insert(1, 'Algorithms', 'HDDA')

    # HDIA
    df_HDIA = pd.read_csv('./save/' + net_data + '/HDIA/reward.csv')
    df_HDIA.columns = col_name
    df_HDIA = df_HDIA.drop(columns=['N', 'ID'])
    df_HDIA.insert(1, 'Algorithms', 'HDIA')

    # FINDER
    df_FINDER = pd.read_csv('./save/' + net_data + '/FINDER/reward.csv')
    df_FINDER.columns = col_name
    df_FINDER = df_FINDER.drop(columns=['N', 'ID'])
    df_FINDER.insert(1, 'Algorithms', 'FINDER')

    # #HBA
    # df_HBA = pd.read_csv('./save/' + net_data + '/HBA/reward.csv')
    # df_HBA.columns = col_name
    # df_HBA = df_HBA.drop(columns=['N', 'ID'])
    # df_HBA.insert(1, 'Algorithms', 'HBA')

    df= pd.concat([df_HDSA,df_HDDA,df_HDIA,df_HDA,df_HPA,df_FINDER,df_SHATTER],axis=0)

    df.to_csv('./save/'+net_data+'/Algorithm Comparison.csv')
