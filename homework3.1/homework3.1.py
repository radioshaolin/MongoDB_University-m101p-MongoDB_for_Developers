#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-11 16:53:47
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-11 17:34:41


import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db = connection.school
students = db.students


def find_lowest_homework():

    query = {'scores.type' : 'homework'}

    try:
        cursor = students.find(query)

        for doc in cursor:
            other_scores = [score for score in doc['scores'] if score['type'] != 'homework']
            homework_scores = [score for score in doc['scores'] if score['type'] == 'homework']
            homework_scores = sorted(homework_scores)[1:]
            new_list = other_scores + homework_scores
            #print new_list
            students.update({'_id': doc['_id']}, {'$set': {'scores': new_list}})

    except Exception as e:
        print "Unexpected error:", type(e), e


if __name__ == "__main__":
    find_lowest_homework()
