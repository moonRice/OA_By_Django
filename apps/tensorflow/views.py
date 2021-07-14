# from django.shortcuts import render
# from django.views import View
#
# import tensorflow as tf
#
#
# # Create your views here.
#
#
# class showIdx(View):
#     def get(self, request):
#         mnist = tf.keras.datasets.mnist
#
#         (x_train, y_train), (x_test, y_test) = mnist.load_data()
#         x_train, x_test = x_train / 255.0, x_test / 255.0
#         model = tf.keras.models.Sequential([
#             tf.keras.layers.Flatten(input_shape=(28, 28)),
#             tf.keras.layers.Dense(128, activation='relu'),
#             tf.keras.layers.Dropout(0.2),
#             tf.keras.layers.Dense(10, activation='softmax')
#         ])
#
#         model.compile(optimizer='adam',
#                       loss='sparse_categorical_crossentropy',
#                       metrics=['accuracy'])
#         model.fit(x_train, y_train, epochs=5)
#
#         re = model.evaluate(x_test, y_test, verbose=2)
#
#         context = {
#             'msg': 'Welcome To Tensorflow!',
#             're': re,
#         }
#         return render(request, 'tensorflow/idx.html', context)
#
#     def post(self, request):
#         pass