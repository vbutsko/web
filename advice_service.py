from sanic import Sanic, response
from bson.objectid import ObjectId
import pymongo
import random


def generate_advice_links(challenge_id, advice_id):
    links = {
        'self': '/'.join(['/advices', challenge_id, advice_id]),
        'random_advice': '/'.join(['advices', challenge_id])
    }
    return links


def generate_random_advice_links(challenge_id, advice_id):
    links = {'self': '/'.join(['/advices', challenge_id]),
             'advice': '/'.join(['/advices', challenge_id, advice_id]),
             'new_advice': '/'.join(['/advice', challenge_id, 'new'])}
    return links


client = pymongo.MongoClient('localhost', 27017)

mydb = client.mydb

advices_collection = mydb.advices

advice_service = Sanic()


@advice_service.route('/hello', methods=['GET'])
async def index(request):
    return response.json({'message': 'Hello, world!'})


@advice_service.route('/advices/<challenge_id:string>', methods=['GET'])
async def advices_challenge_random(request, challenge_id):
    print(challenge_id)
    advice_ids = [doc['_id'] for doc in advices_collection.find({'challenge_id': challenge_id}, {'_id': 1})]
    advice_id = random.choice(advice_ids)
    result = advices_collection.find_one({'_id': advice_id}, {'_id': 0})
    result['_links'] = generate_random_advice_links(challenge_id, str(advice_id))
    return response.text(result, content_type='application/hal+json')


@advice_service.route('/advices/<challenge_id:string>/new', methods=['POST'])
async def advices_challenge_new(request, challenge_id):
    challenge_title = advices_collection.find_one({'challenge_id': challenge_id}, {'challenge_title': 1})[
        'challenge_title']
    doc = {'challenge_id': challenge_id, 'challenge_title': challenge_title,
           'advice_text': request.json['advice_text']}
    advices_collection.save(doc)
    return response.redirect('/'.join(['/advices', challenge_id, str(doc['_id'])]))


@advice_service.route('/advices/<challenge_id:string>/<advice_id:string>')
async def advices_challenge(request, challenge_id, advice_id):
    result = advices_collection.find_one({'_id': ObjectId(advice_id), 'challenge_id': challenge_id}, {'_id': 0})
    result['_links'] = generate_advice_links(challenge_id, advice_id)
    return response.text(result, content_type='application/hal+json')


if __name__ == '__main__':
    advice_service.run(host='0.0.0.0', port=8000)
