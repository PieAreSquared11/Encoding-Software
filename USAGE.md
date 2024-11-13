# How to use this Code

- Simply instantiate an Interpret class and save it to a variable, like so:
- 
  ```code
  interpret = Interpret("key.txt")
  ```
  
- Then save an instance of the Encode Class:
  
  ```code
  encode = Encode(interpret.key, "hello")
  ```

- Then you can print the result:

  ```code
  print(encode.string_data)
  ```

- When you are ready to decode the data, you must create a new Decode class:

  ```code
  decode = Decode(interpret.key, encode.string_data)
  ```

- Then print the decoded data:

  ```code
  print(decode.string_data)
  ```

- All together:

  ```code
  interpret = Interpret("key.txt")

  encode = Encode(interpret.key, "hello")

  print(encode.string_data)

  decode = Decode(interpret.key, encode.string_data)

  print(decode.string_data)

- **NOTE**:
  - After the first 30 characters or so, the encoding will start to make errors, such as removing spaces and miscalculating letters. I will try to fix this mistake.
