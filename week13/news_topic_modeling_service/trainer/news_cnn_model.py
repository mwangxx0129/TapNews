import tensorflow as tf

EMBEDDING_SIZE = 40
N_FILTERS = 10
WINDOW_SIZE = 20
FILTER_SHAPE1 = [WINDOW_SIZE, EMBEDDING_SIZE]
FILTER_SHAPE2 = [WINDOW_SIZE, N_FILTERS]
POOLING_WINDOW = 4
POOLING_STRIDE = 2

LEARNING_RATE = 0.05

def generate_cnn_model(n_classes, n_words):
    """2 layer ConvNet to predict from sequence of words to a class."""
    def cnn_model(features, target):
      # Convert indexes of words into embeddings.
      # This creates embeddings matrix of [n_words, EMBEDDING_SIZE] and then
      # maps word indexes of the sequence into [batch_size, sequence_length,
      # EMBEDDING_SIZE].

      target = tf.one_hot(target, n_classes, 1, 0)
      word_vectors = tf.contrib.layers.embed_sequence(
          features, vocab_size=n_words, embed_dim=EMBEDDING_SIZE, scope='words')
      word_vectors = tf.expand_dims(word_vectors, 3)
      with tf.variable_scope('CNN_layer1'):
        # Apply Convolution filtering on input sequence.
        conv1 = tf.contrib.layers.convolution2d(
            word_vectors, N_FILTERS, FILTER_SHAPE1, padding='VALID')
        # Add a RELU for non linearity.
        conv1 = tf.nn.relu(conv1)
        # Max pooling across output of Convolution+Relu.
        pool1 = tf.nn.max_pool(
            conv1,
            ksize=[1, POOLING_WINDOW, 1, 1],
            strides=[1, POOLING_STRIDE, 1, 1],
            padding='SAME')
        # Transpose matrix so that n_filters from convolution becomes width.
        pool1 = tf.transpose(pool1, [0, 1, 3, 2])
      with tf.variable_scope('CNN_layer2'):
        # Second level of convolution filtering.
        conv2 = tf.contrib.layers.convolution2d(
            pool1, N_FILTERS, FILTER_SHAPE2, padding='VALID')
        # Max across each filter to get useful features for classification.
        pool2 = tf.squeeze(tf.reduce_max(conv2, 1), squeeze_dims=[1])

      # Apply regular WX + B and classification.
      logits = tf.contrib.layers.fully_connected(pool2, n_classes, activation_fn=None)
      loss = tf.contrib.losses.softmax_cross_entropy(logits, target)

      train_op = tf.contrib.layers.optimize_loss(
          loss,
          tf.contrib.framework.get_global_step(),
          optimizer='Adam',
          learning_rate=LEARNING_RATE)

      return ({
          'class': tf.argmax(logits, 1),
          'prob': tf.nn.softmax(logits)
      }, loss, train_op)

    return cnn_model