# coding=utf-8
from __future__ import division
import os
import math
import datetime
# 维数为11089


def Vector():
    # dir_export_url_pos = dir_export_url_temp_pos.replace('\\', '/')
    # file_import_url_neg = file_import_url_temp_neg.replace('\\', '/')
    # file_export_url_neg = file_export_url_temp_neg.replace('\\', '/')
    start_time = datetime.datetime.now()
    print start_time
    word_in_a_file_stat = {}
    word_in_all_file_stat = {}
    files_num = 0
    listfile_1 = os.listdir(os.getcwd())
    for line_1 in listfile_1:
        if line_1 == 'vector.py' or line_1 == '.vscode':
            continue
        else:
            listfile_2 = os.listdir(os.getcwd() + "/" + line_1)
            for line_2 in listfile_2:
                listfile_3 = os.listdir(
                    os.getcwd() + "/" + line_1 + '/' + line_2)
                for line_3 in listfile_3:
                    listfile_4 = os.listdir(
                        os.getcwd() + '/' + line_1 + '/' + line_2 + '/' + line_3)
                    for line in listfile_4:
                        if line[:12] != "no_filename_":
                            with open(os.getcwd() + '/' + line_1 + '/' + line_2 + '/' + line_3 + '/' + line,
                                      'r') as data_source_pos:
                                data_pos = data_source_pos.readline().replace('\n', ' ')
                                while (data_pos != ''):
                                    data_temp_1 = []
                                    files_num += 1
                                    data_temp_2 = []
                                    # file name and key words of a file
                                    data_temp_1 = data_pos.split("\t")
                                    data_temp_2 = data_temp_1[1].split(
                                        " ")  # key words of a file
                                    file_name = data_temp_1[0]
                                    data_temp_len = len(data_temp_2)
                                    files_num += 1
                                    for word in data_temp_2:
                                        if word in data_temp_2:
                                            if not word in word_in_all_file_stat:
                                                word_in_all_file_stat[word] = 1
                                                # 若词没有出现过，初始化此词在文档出现次数为1
                                            else:
                                                word_in_all_file_stat[
                                                    word] += 1
                                                # 若词出现过，将此词在文档中出现的次数加1
                                            if not file_name in word_in_a_file_stat:
                                                word_in_a_file_stat[
                                                    file_name] = {}
                                                # 初始化在当前文档出现词的一个数组
                                            if not word in word_in_a_file_stat[file_name]:
                                                word_in_a_file_stat[
                                                    file_name][word] = []
                                                # 初始化当前词数组
                                                word_in_a_file_stat[file_name][
                                                    word].append(data_temp_2.count(word))
                                                # 将此词的出现次数放入数组
                                                word_in_a_file_stat[file_name][
                                                    word].append(data_temp_len)
                                                # 将此词所出现的文档的总词数放入数组
                                    data_pos = data_source_pos.readline()
    # print files_num

    listfile_1 = os.listdir(os.getcwd())
    n = 0
    for line_1 in listfile_1:
        if line_1 == 'vector.py' or line_1 == '.vscode':
            continue
        else:
            listfile_2 = os.listdir(os.getcwd() + '/' + line_1)
            for line_2 in listfile_2:
                listfile_3 = os.listdir(
                    os.getcwd() + '/' + line_1 + '/' + line_2)
                for line_3 in listfile_3:
                    listfile_4 = os.listdir(
                        os.getcwd() + '/' + line_1 + '/' + line_2 + '/' + line_3)
                    for line in listfile_4:
                        if line[:12] != "no_filename_":
                            with open('E:/code/opsam_vector' + '/' + line_1 + '/' + line_2 + '/' + line_3 + '/' + line,
                                    'w+') as target:
                                result_temp = []
                                if (word_in_a_file_stat) and (word_in_all_file_stat) and (files_num != 0):
                                    TF_IDF_result = {}
                                    for all_word in word_in_all_file_stat:
                                        if '' == all_word:
                                            continue
                                        TF_IDF_result[all_word] = 0
                                        for word in word_in_a_file_stat[line].keys():
                                            if '' == word:
                                                continue
                                            word_n = word_in_a_file_stat[
                                                line][word][0]
                                            # 单个文档中的单个词的个数
                                            word_sum = word_in_a_file_stat[
                                                line][word][1]
                                            # 单个文档的总词数
                                            with_word_sum = word_in_all_file_stat[
                                                word]
                                            # 拥有同一个词的文档数
                                            # for filename in word_in_a_file_stat.keys():
                                            #     TF_IDF_result[filename]={}
                                            #     for all_word in word_in_all_file_stat.keys():
                                            #         TF_IDF_result[all_word]=0
                                            #         for word in word_in_a_file_stat[filename].keys():
                                            #             word_n = word_in_a_file_stat[filename][word][0]
                                            #             # 单个文档中的单个词的个数
                                            #             word_sum = word_in_a_file_stat[filename][word][1]
                                            #             # 单个文档的总词数
                                            #             with_word_sum = word_in_all_file_stat[word]
                                            #             # 拥有同一个词的文档数
                                            TF_IDF_result[word] = (
                                                math.exp(word_n / word_sum)) * (math.log10(files_num / with_word_sum))
                                for word in TF_IDF_result.keys():
                                    try:
                                        target.write(
                                            str(TF_IDF_result[word]) + ' ')
                                    except IOError:
                                        print ("IOError")

                                        #             TF_IDF_result[word] = ((word_n / word_sum)) * (math.log10(files_num / with_word_sum))

                                        #     target.write(str(TF_IDF_result[all_word]))
                                        #     target.write(" ")
                                        # target.write("\n")
    end_time=datetime.datetime.now()
    last_time=end_time-start_time
    print end_time
    print last_time


def run():
    Vector()


if __name__ == '__main__':
    run()
