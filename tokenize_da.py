# coding=utf-8
from __future__ import division
import jieba as jb
import math
import os
def tokenize(input_pos_dir_url_temp,output_pos_dir_url_temp):
    fn = open('english_stopword.dat', 'r')
    stopwords = {}.fromkeys([line.rstrip() for line in fn])
    input_pos_dir_url = input_pos_dir_url_temp.replace('\\', '/')
    # input_neg_dir_url = input_neg_dir_url_temp.replace('\\', '/')
    output_pos_dir_url = output_pos_dir_url_temp.replace('\\', '/')
    # output_neg_file_url = output_neg_file_url_temp.replace('\\', '/')
    listfile_pos = os.listdir(input_pos_dir_url)
    for line_pos in listfile_pos:
        File_pos = open(input_pos_dir_url +'/'+ line_pos, 'r')
        File_pos_data = File_pos.read()
        segs = jb.cut(File_pos_data)
        final = ''
        for seg in segs:
            if seg not in stopwords:
                final += seg
        final = final.replace('\n', ' ')
        final = ' '.join(final.split())
        newfile_with_name = open(output_pos_dir_url+'/'+line_pos, 'a')
        newfile_no_name=open(output_pos_dir_url+'/'+"no_filename_"+line_pos,'a')
        newfile_with_name.write(line_pos)
        newfile_with_name.write("\t")
        newfile_with_name.write(final)
        newfile_no_name.write(final)
        newfile_with_name.write("\n")
        newfile_no_name.write("\n")
        newfile_with_name.close()
        newfile_no_name.close()

    # listfile_neg = os.listdir(input_neg_dir_url)
    # for line_neg in listfile_neg:
    #     File_neg = open(input_neg_dir_url + line_neg, 'r')
    #     File_neg_data = File_neg.read()
    #     segs = jb.cut(File_neg_data)
    #     final = ""
    #     for seg in segs:
    #         if seg not in stopwords:
    #             final += seg
    #     #final = final.replace('\n', ' ')
    #     final = ' '.join(final.split())
    #     newfile_with_name = open(output_neg_file_url+".txt", 'a')
    #     newfile_no_name=open(output_neg_file_url+"_no_filename.txt",'a')
    #     newfile_with_name.write(line_neg)
    #     newfile_with_name.write("\t")
    #     newfile_with_name.write(final)
    #     newfile_no_name.write(final)
    #     newfile_with_name.write("\n")
    #     newfile_no_name.write("\n")
    #     newfile_with_name.close()
    #     newfile_no_name.close()

def Vector(file_import_url_temp_pos,file_export_url_temp_pos):
    file_import_url_pos = file_import_url_temp_pos.replace('\\', '/')
    file_export_url_pos = file_export_url_temp_pos.replace('\\', '/')
    # file_import_url_neg = file_import_url_temp_neg.replace('\\', '/')
    # file_export_url_neg = file_export_url_temp_neg.replace('\\', '/')


    data_source_pos = open(file_import_url_pos, 'r')
    data_pos = data_source_pos.readline()
    word_in_a_file_stat = {}
    word_in_all_file_stat = {}
    files_num = 0
    while(data_pos != ''):
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
    # data_source_neg = open(file_import_url_neg, 'r')
    # data_neg = data_source_neg.readline()
    # files_num = 0
    # while (data_neg != ""):
    #     data_temp_1 = []
    #     data_temp_2 = []
    #     data_temp_1 = data_neg.split("\t")  # file name and key words of a file
    #     data_temp_2 = data_temp_1[1].split(" ")  # key words of a file
    #     file_name = data_temp_1[0]
    #     data_temp_len = len(data_temp_2)
    #     files_num += 1
    #     for word in data_temp_2:
    #         if word in data_temp_2:
    #             if not word in word_in_all_file_stat:
    #                 word_in_all_file_stat[word] = 1
    #                 # 若词没有出现过，初始化此词在文档出现次数为1
    #             else:
    #                 word_in_all_file_stat[word] += 1
    #                 # 若词出现过，将此词在文档中出现的次数加1
    #             if not file_name in word_in_a_file_stat:
    #                 word_in_a_file_stat[file_name] = {}
    #                 # 初始化在当前文档出现词的一个数组
    #             if not word in word_in_a_file_stat[file_name]:
    #                 word_in_a_file_stat[file_name][word] = []
    #                 # 初始化当前词数组
    #                 word_in_a_file_stat[file_name][word].append(data_temp_2.count(word))
    #                 # 将此词的出现次数放入数组
    #                 word_in_a_file_stat[file_name][word].append(data_temp_len)
    #                 # 将此词所出现的文档的总词数放入数组
    #     data_neg = data_source_neg.readline()
    # data_source_neg.close()


    export = open(file_export_url_pos, "w")
    result_temp = []
    if (word_in_a_file_stat) and (word_in_all_file_stat) and (files_num != 0):
        # TF-IDF处理
        TF_IDF_result = {}
        for filename in word_in_a_file_stat.keys():
            TF_IDF_result[filename] = {}
            for all_word in word_in_all_file_stat.keys():
                TF_IDF_result[all_word]=0
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
    # export = open(file_export_url_neg,"w")
    # result_temp = []
    # if (word_in_a_file_stat) and (word_in_all_file_stat) and (files_num != 0):
    #     # TF-IDF处理
    #     TF_IDF_result = {}
    #     for filename in word_in_a_file_stat.keys():
    #         TF_IDF_result[filename] = {}
    #         for all_word in word_in_all_file_stat.keys():
    #             TF_IDF_result[all_word]=0
    #             for word in word_in_a_file_stat[filename].keys():
    #                 word_n = word_in_a_file_stat[filename][word][0]
    #                 # 单个文档中的单个词的个数
    #                 word_sum = word_in_a_file_stat[filename][word][1]
    #                 # 单个文档的总词数
    #                 with_word_sum = word_in_all_file_stat[word]
    #                 # 拥有同一个词的文档数
    #                 # TF_IDF_result[filename][word]=(math.exp(word_n/word_sum))*(math.log10(files_num/with_word_sum))
    #                 TF_IDF_result[word] = ((word_n / word_sum)) * (math.log10(files_num / with_word_sum))
    #             export.write(str(TF_IDF_result[all_word]))
    #             export.write(" ")
    #         export.write("\n")
    # export.close()

def run():
    tokenize("op_spam/negative_polarity/deceptive_from_MTurk/fold1","opsam_tokenize/negative_polarity/deceptive_from_MTurk/fold1")
    tokenize("op_spam/negative_polarity/deceptive_from_MTurk/fold2","opsam_tokenize/negative_polarity/deceptive_from_MTurk/fold2")
    tokenize("op_spam/negative_polarity/deceptive_from_MTurk/fold3","opsam_tokenize/negative_polarity/deceptive_from_MTurk/fold3")
    tokenize("op_spam/negative_polarity/deceptive_from_MTurk/fold4","opsam_tokenize/negative_polarity/deceptive_from_MTurk/fold4")
    tokenize("op_spam/negative_polarity/deceptive_from_MTurk/fold5","opsam_tokenize/negative_polarity/deceptive_from_MTurk/fold5")
    tokenize("op_spam/negative_polarity/truthful_from_Web/fold1","opsam_tokenize/negative_polarity/truthful_from_Web/fold1")
    tokenize("op_spam/negative_polarity/truthful_from_Web/fold2","opsam_tokenize/negative_polarity/truthful_from_Web/fold2")
    tokenize("op_spam/negative_polarity/truthful_from_Web/fold3","opsam_tokenize/negative_polarity/truthful_from_Web/fold3")
    tokenize("op_spam/negative_polarity/truthful_from_Web/fold4","opsam_tokenize/negative_polarity/truthful_from_Web/fold4")
    tokenize("op_spam/negative_polarity/truthful_from_Web/fold5","opsam_tokenize/negative_polarity/truthful_from_Web/fold5")
    tokenize("op_spam/positive_polarity/deceptive_from_MTurk/fold1","opsam_tokenize/positive_polarity/deceptive_from_MTurk/fold1")
    tokenize("op_spam/positive_polarity/deceptive_from_MTurk/fold2","opsam_tokenize/positive_polarity/deceptive_from_MTurk/fold2")
    tokenize("op_spam/positive_polarity/deceptive_from_MTurk/fold3","opsam_tokenize/positive_polarity/deceptive_from_MTurk/fold3")
    tokenize("op_spam/positive_polarity/deceptive_from_MTurk/fold4","opsam_tokenize/positive_polarity/deceptive_from_MTurk/fold4")
    tokenize("op_spam/positive_polarity/deceptive_from_MTurk/fold5","opsam_tokenize/positive_polarity/deceptive_from_MTurk/fold5")
    tokenize("op_spam/positive_polarity/truthful_from_TripAdvisor/fold1","opsam_tokenize/positive_polarity/truthful_from_TripAdvisor/fold1")
    tokenize("op_spam/positive_polarity/truthful_from_TripAdvisor/fold2","opsam_tokenize/positive_polarity/truthful_from_TripAdvisor/fold2")
    tokenize("op_spam/positive_polarity/truthful_from_TripAdvisor/fold3","opsam_tokenize/positive_polarity/truthful_from_TripAdvisor/fold3")
    tokenize("op_spam/positive_polarity/truthful_from_TripAdvisor/fold4","opsam_tokenize/positive_polarity/truthful_from_TripAdvisor/fold4")
    tokenize("op_spam/positive_polarity/truthful_from_TripAdvisor/fold5","opsam_tokenize/positive_polarity/truthful_from_TripAdvisor/fold5")
if __name__ == '__main__':
    run()