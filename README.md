# 5'-ACGT-3'

*when combine the nucleobase with the multi-level cell*

## Whats this project?

It's a binary-to-text encoding scheme, like base64, which encode the binary data into the printable character, in this projeet, the nucleobase found in DNA.

## How to use this?

```python
>>> import acgt
>>> input = acgt.acgt('你好')
>>> input.encode()
'TGCAGTTCGGAATGCCGGCCGTTC'
>>> input = acgt.acgt('TGCAGTTCGGAATGCCGGCCGTTC')
>>> input.decode()
'你好'
>>> 
```

## Why this?

I don't quite sure where i can use it. This scheme has taken up times of space than original message.

But may useful when needed to transform *unwelcome information* in the videos when uploading to the video platform...I'll test it someday.

## The future?

 [ ] As mentioned, to accept custom letter, or words?

## License

MIT
