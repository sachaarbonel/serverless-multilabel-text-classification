import magpie
# try:
#     import unzip_requirements
# except ImportError:
#     pass

# #import json
# import tensorflow as tf
# import logging

# logger = logging.getLogger()
# if logger.handlers:
#     for handler in logger.handlers:
#         logger.removeHandler(handler)
# logging.basicConfig(level=logging.INFO)

# def add(event, context):

#     logger.info('Event : {}'.format(event))
#     logger.info('Event a : {}'.format(event['a']))

#     a = tf.constant(event['a'])
#     b = tf.constant(event['b'])

#     result = tf.Session().run(tf.add(a, b))

#     return {
#         "message": "TensorFlow \"add\" function test: {} + {}".format(event['a'], event['b']),
#         "result": "{}".format(result)
#     }


#     if __name__ == "__main__":
#         main('', '')