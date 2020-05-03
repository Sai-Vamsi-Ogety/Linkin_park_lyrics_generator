import numpy as np  
from dataset import char2idx, lyrics_joined

def create_batch(vectorized_songs, seq_length, batch_size):

	#vectorize the song
	vectorized_lyrics = np.array([char2idx[x] for x in lyrics_joined])
	n = vectorized_lyrics.shape[0] - 1

	idx = np.random.choice(n-seq_length, batch_size)
	input_batch = [vectorized_lyrics[ i:i+seq_length] for i in idx]
	output_batch = [vectorized_lyrics[i+1:i+seq_length+1] for i in idx]

	x_batch = np.reshape(input_batch, [batch_size, seq_length])
	y_batch = np.reshape(output_batch, [batch_size, seq_length])

	return x_batch,y_batch

if __name__ == "__main__":
	create_batch()

	


