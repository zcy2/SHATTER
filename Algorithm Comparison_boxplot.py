import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
networks=['scalefree','random','smallworld']
for net in networks:

    df1 = pd.read_csv('./save/network_'+net+'_90-150/Algorithm Comparison.csv')
    # df1['ANC']= df1['ANC'].apply(lambda x: x / 3)
    df2 = pd.read_csv('./save/network_'+net+'_150-300/Algorithm Comparison.csv')
    # df2['ANC']= df2['ANC'].apply(lambda x: x / 3)
    df3 = pd.read_csv('./save/network_'+net+'_300-600/Algorithm Comparison.csv')
    # df3['ANC']= df3['ANC'].apply(lambda x: x / 3)
    df4 = pd.read_csv('./save/network_'+net+'_600-900/Algorithm Comparison.csv')
    # df4['ANC']= df4['ANC'].apply(lambda x: x / 3)
    # print(df.describe())
    # Draw Plot

    plt.figure(figsize=(20, 15), dpi=200)

    plt.subplot(221)
    sns.boxplot(x='Algorithms',y='ANOC',palette="Set1",width=0.8,data=df1,showfliers=False,saturation=0.5)
    plt.title('90-150',fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel('',fontsize = 20)  # 添加x轴的名称
    plt.ylabel('ANOC', fontsize=20)

    plt.subplot(222)
    sns.boxplot(x='Algorithms',y='ANOC',palette="Set1",width=0.8,data=df2,showfliers=False,saturation=0.5)
    plt.title('150-300',fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel('', fontsize=20)  # 添加x轴的名称
    plt.ylabel('ANOC', fontsize=20)

    plt.subplot(223)
    sns.boxplot(x='Algorithms',y='ANOC',palette="Set1",width=0.8,data=df3,showfliers=False,saturation=0.5)
    plt.title('300-600',fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel('', fontsize=20)  # 添加x轴的名称
    plt.ylabel('ANOC', fontsize=20)

    plt.subplot(224)
    sns.boxplot(x='Algorithms',y='ANOC',palette="Set1",width=0.8,data=df4,showfliers=False,saturation=0.5)
    plt.title('600-900',fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel('', fontsize=20)  # 添加x轴的名称
    plt.ylabel('ANOC', fontsize=20)

    # Decoration
    # plt.title('Performance of Different Algorithms on Different Size Test Networks', fontsize=18)
    # plt.tight_layout()
    # plt.show()
    # plt.savefig('./save/pic.png', bbox_inches='tight')
    # plt.savefig('./save/pic.svg', format='svg', bbox_inches='tight')
    # plt.show()
    plt.savefig('./save/Algorithm_Comparison_'+net+'.png', format='png', bbox_inches='tight')