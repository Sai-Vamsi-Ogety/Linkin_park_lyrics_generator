
import numpy as np
def main():

	lyrics_file = open("../input/linkinpark_lyrics_v1.txt","r")
	lyrics = lyrics_file.read()

	print("Example song lyrics:")
	print(lyrics[:100])

	lyrics_joined = "\n\n".join(lyrics)

	vocab = sorted(set(lyrics_joined))
	print("There are {} unique characters in the dataset".format(len(vocab)))

	char2idx = {u:i for i,u in enumerate(vocab)}
	idx2char = np.array(vocab)

	for char, _ in zip(char2idx, range(20)):
		print("{} : {}".format(repr(char), char2idx[char]))

if __name__ == "__main__":
	main()
