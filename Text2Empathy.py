#Copyright [zashio]

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "C:***/***/***.json"


"""Analyzes text using the Google Cloud Natural Language API."""

import argparse
import json
import sys

import googleapiclient.discovery


def get_native_encoding_type():
    """Returns the encoding type that matches Python's native strings."""
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'


def analyze_entities(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding,
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeEntities(body=body)
    response = request.execute()

    return response


def analyze_sentiment(text, encoding='utf-8'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeSentiment(body=body)
    response = request.execute()

    return response


def analyze_syntax(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeSyntax(body=body)
    response = request.execute()

    return response


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=[
        'entities', 'sentiment', 'syntax'])
    parser.add_argument('filename')

    args = parser.parse_args()

    mail_contents = ''
    with open(args.filename, encoding = 'utf-8') as f:
        for line in f:
            line = line.rstrip()
            mail_contents += line

    print(mail_contents)

    if args.command == 'entities':
        result = analyze_entities(mail_contents, get_native_encoding_type())
    elif args.command == 'sentiment':
        result = analyze_sentiment(mail_contents, get_native_encoding_type())
    elif args.command == 'syntax':
        result = analyze_syntax(mail_contents, get_native_encoding_type())

    print(json.dumps(result, indent=2))