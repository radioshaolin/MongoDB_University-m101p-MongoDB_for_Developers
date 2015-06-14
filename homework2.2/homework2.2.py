#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-07 00:53:47
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-07 01:58:25


import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db = connection.students
grades = db.grades


def find():

    query = {'type' : 'homework'}
    sorting_query = ['student_id', 'score']

    try:
        cursor = grades.find(query)\
        .sort([(sorting_query[0], pymongo.ASCENDING),\
               (sorting_query[1], pymongo.ASCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    previous_id = None
    student_id = None

    for doc in cursor:
        student_id = doc['student_id']
        if student_id != previous_id:
            previous_id = student_id
            print "Removing", doc
            grades.remove({ '_id' : doc['_id'] })


if __name__ == "__main__":
    find()
