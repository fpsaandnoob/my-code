# coding=utf-8
# ***************************************
#          PU Framework
#         HLC  in  SICAU
#      Created in 2016/12/25
#      Vector module error:Sovled
# ***************************************

from __future__ import division
import math
import os
import sys
import jieba as jb
import numpy as np
from sklearn import mixture

reload(sys)
sys.setdefaultencoding('utf-8')
np.set_printoptions(threshold='nan')
Alpha = 16
Beta = 4
P_COUNT = 80
dim = 11089


def tokenize(input_pos_dir_url_temp, input_neg_dir_url_temp, output_pos_file_url_temp, output_neg_file_url_temp):
    fn = open('english_stopword.dat', 'r')
    stopwords = {}.fromkeys([line.rstrip() for line in fn])
    input_pos_dir_url = input_neg_dir_url_temp.replace('\\', '/')
    input_neg_dir_url = input_neg_dir_url_temp.replace('\\', '/')
    output_pos_file_url = output_pos_file_url_temp.replace('\\', '/')
    output_neg_file_url = output_neg_file_url_temp.replace('\\', '/')
    listfile_pos = os.listdir(input_pos_dir_url)
    for line_pos in listfile_pos:
        File_pos = open(input_pos_dir_url + line_pos, 'r')
        File_pos_data = File_pos.read()
        segs = jb.cut(File_pos_data)
        final = ''
        for seg in segs:
            if seg not in stopwords:
                final += seg
        final = final.replace('\n', ' ')
        final = ' '.join(final.split())
        newfile_with_name = open(output_pos_file_url + ".txt", 'a')
        newfile_no_name = open(output_pos_file_url + "_no_filename.txt", 'a')
        newfile_with_name.write(line_pos)
        newfile_with_name.write("\t")
        newfile_with_name.write(final)
        newfile_no_name.write(final)
        newfile_with_name.write("\n")
        newfile_no_name.write("\n")
        newfile_with_name.close()
        newfile_no_name.close()

    listfile_neg = os.listdir(input_neg_dir_url)
    for line_neg in listfile_neg:
        File_neg = open(input_neg_dir_url + line_neg, 'r')
        File_neg_data = File_neg.read()
        segs = jb.cut(File_neg_data)
        final = ""
        for seg in segs:
            if seg not in stopwords:
                final += seg
        # final = final.replace('\n', ' ')
        final = ' '.join(final.split())
        newfile_with_name = open(output_neg_file_url + ".txt", 'a')
        newfile_no_name = open(output_neg_file_url + "_no_filename.txt", 'a')
        newfile_with_name.write(line_neg)
        newfile_with_name.write("\t")
        newfile_with_name.write(final)
        newfile_no_name.write(final)
        newfile_with_name.write("\n")
        newfile_no_name.write("\n")
        newfile_with_name.close()
        newfile_no_name.close()


def Vector(file_import_url_temp_pos, file_import_url_temp_neg, file_export_url_temp_pos, file_export_url_temp_neg):
    file_import_url_pos = file_import_url_temp_pos.replace('\\', '/')
    file_export_url_pos = file_export_url_temp_pos.replace('\\', '/')
    file_import_url_neg = file_import_url_temp_neg.replace('\\', '/')
    file_export_url_neg = file_export_url_temp_neg.replace('\\', '/')

    data_source_pos = open(file_import_url_pos, 'r')
    data_pos = data_source_pos.readline()
    word_in_a_file_stat = {}
    word_in_all_file_stat = {}
    files_num = 0
    while (data_pos != ''):
        data_temp_1 = []
        data_temp_2 = []
        data_temp_1 = data_pos.split("\t")  # file name and key words of a file
        data_temp_2 = data_temp_1[1].split(" ")  # key words of a file
        file_name = data_temp_1[0]
        data_temp_len = len(data_temp_2)
        files_num += 1
        for word in data_temp_2:
            if word in data_temp_2:
                if not word in word_in_all_file_stat:
                    word_in_all_file_stat[word] = 1
                    # 若词没有出现过，初始化此词在文档出现次数为1
                else:
                    word_in_all_file_stat[word] += 1
                    # 若词出现过，将此词在文档中出现的次数加1
                if not file_name in word_in_a_file_stat:
                    word_in_a_file_stat[file_name] = {}
                    # 初始化在当前文档出现词的一个数组
                if not word in word_in_a_file_stat[file_name]:
                    word_in_a_file_stat[file_name][word] = []
                    # 初始化当前词数组
                    word_in_a_file_stat[file_name][word].append(data_temp_2.count(word))
                    # 将此词的出现次数放入数组
                    word_in_a_file_stat[file_name][word].append(data_temp_len)
                    # 将此词所出现的文档的总词数放入数组
        data_pos = data_source_pos.readline()
    data_source_pos.close()
    data_source_neg = open(file_import_url_neg, 'r')
    data_neg = data_source_neg.readline()
    files_num = 0
    while data_neg != "":
        data_temp_1 = []
        data_temp_2 = []
        data_temp_1 = data_neg.split("\t")  # file name and key words of a file
        data_temp_2 = data_temp_1[1].split(" ")  # key words of a file
        file_name = data_temp_1[0]
        data_temp_len = len(data_temp_2)
        files_num += 1
        for word in data_temp_2:
            if word in data_temp_2:
                if not word in word_in_all_file_stat:
                    word_in_all_file_stat[word] = 1
                    # 若词没有出现过，初始化此词在文档出现次数为1
                else:
                    word_in_all_file_stat[word] += 1
                    # 若词出现过，将此词在文档中出现的次数加1
                if not file_name in word_in_a_file_stat:
                    word_in_a_file_stat[file_name] = {}
                    # 初始化在当前文档出现词的一个数组
                if not word in word_in_a_file_stat[file_name]:
                    word_in_a_file_stat[file_name][word] = []
                    # 初始化当前词数组
                    word_in_a_file_stat[file_name][word].append(data_temp_2.count(word))
                    # 将此词的出现次数放入数组
                    word_in_a_file_stat[file_name][word].append(data_temp_len)
                    # 将此词所出现的文档的总词数放入数组
        data_neg = data_source_neg.readline()
    data_source_neg.close()

    export = open(file_export_url_pos, "w")
    if word_in_a_file_stat and word_in_all_file_stat and (files_num != 0):
        # TF-IDF处理
        TF_IDF_result = {}
        for filename in word_in_a_file_stat.keys():
            TF_IDF_result[filename] = {}
            for all_word in word_in_all_file_stat.keys():
                TF_IDF_result[all_word] = 0
                for word in word_in_a_file_stat[filename].keys():
                    word_n = word_in_a_file_stat[filename][word][0]
                    # 单个文档中的单个词的个数
                    word_sum = word_in_a_file_stat[filename][word][1]
                    # 单个文档的总词数
                    with_word_sum = word_in_all_file_stat[word]
                    # 拥有同一个词的文档数
                    # TF_IDF_result[filename][word]=(math.exp(word_n/word_sum))*(math.log10(files_num/with_word_sum))
                    TF_IDF_result[word] = ((word_n / word_sum)) * (math.log10(files_num / with_word_sum))
                export.write(str(TF_IDF_result[all_word]))
                export.write(" ")
            export.write("\n")
    export.close()
    export = open(file_export_url_neg, "w")
    if word_in_a_file_stat and word_in_all_file_stat and (files_num != 0):
        # TF-IDF处理
        TF_IDF_result = {}
        for filename in word_in_a_file_stat.keys():
            TF_IDF_result[filename] = {}
            for all_word in word_in_all_file_stat.keys():
                TF_IDF_result[all_word] = 0
                for word in word_in_a_file_stat[filename].keys():
                    word_n = word_in_a_file_stat[filename][word][0]
                    # 单个文档中的单个词的个数
                    word_sum = word_in_a_file_stat[filename][word][1]
                    # 单个文档的总词数
                    with_word_sum = word_in_all_file_stat[word]
                    # 拥有同一个词的文档数
                    # TF_IDF_result[filename][word]=(math.exp(word_n/word_sum))*(math.log10(files_num/with_word_sum))
                    TF_IDF_result[word] = ((word_n / word_sum)) * (math.log10(files_num / with_word_sum))
                export.write(str(TF_IDF_result[all_word]))
                export.write(" ")
            export.write("\n")
    export.close()


def TopicUnion(file_theta_url_temp, file_export_url_temp):
    file_import_url = file_theta_url_temp.replace('\\', '/')
    file_export_url = file_export_url_temp.replace('\\', '/')
    theta_srcfile = open(file_import_url, 'r')
    theta_temp = theta_srcfile.readline()
    Topicfile_src = open(file_export_url, 'w')
    while (theta_temp != ''):
        theta_data = np.fromstring(theta_temp, sep=' ')
        theta_max = np.argmax(theta_data)
        theta_temp = theta_srcfile.readline()
        Topicfile_src.write(str(theta_max) + '\n')
        # print theta_max
    theta_srcfile.close()
    # Topicfile_src.close()


def FileMatch(list_file_temp, doc_srcfile_temp):
    list_file = open(list_file_temp, 'r')
    doc_srcfile = open(doc_srcfile_temp, 'r')
    count = list_file.readline()
    doc_temp = doc_srcfile.readline()
    while count != '':
        if '0\n' == count:
            doc_finfile = open("topic/t0.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '1\n' == count:
            doc_finfile = open("topic/t1.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '2\n' == count:
            doc_finfile = open("topic/t2.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '3\n' == count:
            doc_finfile = open("topic/t3.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '4\n' == count:
            doc_finfile = open("topic/t4.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '5\n' == count:
            doc_finfile = open("topic/t5.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '6\n' == count:
            doc_finfile = open("topic/t6.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '7\n' == count:
            doc_finfile = open("topic/t7.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '8\n' == count:
            doc_finfile = open("topic/t8.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
        elif '9\n' == count:
            doc_finfile = open("topic/t9.txt", 'a+')
            doc_finfile.write(doc_temp)
            # print count
            count = list_file.readline()
            doc_temp = doc_srcfile.readline()
            doc_finfile.close()
    list_file.close()
    doc_srcfile.close()
    # print ('1')


def algorithm1():
    RN_Data = []
    RN_Count = []
    RN_VECTOR_DATA = np.zeros((dim,))
    ListFile = os.listdir("topic")
    for line in ListFile:
        RN_VECTOR_COUNT = 0
        Neg_Data_Src = open("topic/" + line, 'r')
        Neg_Data_Temp = Neg_Data_Src.readline()
        while Neg_Data_Temp != '':
            # Vector_data_temp=np.zeros((400,),dtype=np.float32)
            Neg_Vector_data_temp = np.fromstring(Neg_Data_Temp, sep=' ')
            Neg_Vector_data = Neg_Vector_data_temp / (np.sqrt(np.sum(Neg_Vector_data_temp*Neg_Vector_data_temp)))
            Neg_Data_Temp = Neg_Data_Src.readline()
            RN_VECTOR_DATA += Neg_Vector_data
            RN_VECTOR_COUNT += 1
            print len(RN_VECTOR_DATA)
            print RN_VECTOR_COUNT
            # print (np.abs(RN_VECTOR_DATA))
        Neg_Data_Src.close()
        RN_Count.append(RN_VECTOR_COUNT)
        RN_Data.append(RN_VECTOR_DATA)

        RN_VECTOR_DATA = np.zeros((dim,))
    Pos_Data_Src = open("finished_pos.dat", 'r')
    Pos_Data_Temp = Pos_Data_Src.readline()
    P_VECTOR_DATA = np.zeros((dim,))
    while Pos_Data_Temp != '':
        Pos_Vector_data_temp = np.fromstring(Pos_Data_Temp, sep=' ')
        Pos_Vector_data = Pos_Vector_data_temp / (np.sqrt(np.sum(Pos_Vector_data_temp*Pos_Vector_data_temp)))
        Pos_Data_Temp = Pos_Data_Src.readline()
        P_VECTOR_DATA += Pos_Vector_data
    Pos_Data_Src.close()
    P_value = []
    N_value = []
    for n in range(10):
        P_value_temp = ((Alpha * P_VECTOR_DATA) / P_COUNT) - ((Beta * RN_Data[n]) / RN_Count[n])
        P_value.append(P_value_temp)
        N_value_temp = ((Alpha * RN_Data[n]) / RN_Count[n]) - ((Beta * P_VECTOR_DATA) / P_COUNT)
        N_value.append(N_value_temp)
        # print N_value
        # P_data_file.write(str(P_value))
        # P_data_file.write("\n")
        # N_data_file.write(str(N_value))
        # N_data_file.write("\n")
    np.save('P_data', P_value)
    np.save('N_data', N_value)


def dpmm():
    data_file = np.fromfile("finished_pos.dat")
    print (data_file)
    mixture.DPGMM().fit(data_file)
    print data_file


def run():
    # Vector("doc/pos.txt","doc/neg.txt","finished_pos.dat","finished_neg.dat")
    # TopicUnion("model_theta.dat", "TopicUnion_neg.dat")
    FileMatch("TopicUnion_neg.dat", "finished_neg.dat")
    algorithm1()


if __name__ == '__main__':
    run()
    # dpmm()
