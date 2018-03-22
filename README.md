# Ling10
A dataset of 190 000 sentences categorized into 10 languages, primarily for Language Detection and Benchmarking NLP Algorithms. This repository containes the dataset and code for processing it.
<hr>
<h1> Purpose </h1>
<div style="font-family: 30px Calibri;" ><br><span>
        This dataset is meant for use by researchers aiming to use machine learning techniques to build automatic language detection algorithms.<br>
  It is also aimed at Evaluating the general effectiveness of newly developed Techniques for Natural Language Processing.
  This is a well organized Benchmark and we hope you find this useful in your research works.
  </b> 
  
  
  
<h3>Structure</h3>
<hr>
Ling10 is released in three variants
 <ul>
  <li>
  Ling10-trainlarge: Contains 140 000 sentences (14 000 per language class) for training and 50 000 sentences (5000 per language class) for testing
  </li>
  <li>
   Ling10-trainmedium: Contains 95 000 sentences (9500 per language class) for training and 95 000 sentences (9500 per language class) for testing
  </li>
  <li>
   Ling10-trainsmall: Contains 20 000 sentences (2000 per language class) for training and 170 000 sentences (17000 per language class) for testing. This is much more challenging dataset
  </li>
  </ul>
    
Each Variant contains the following files
 
<h3>train_set.txt</h3>
	Contains sentences for training and integer labels representing the language classes

<h3>test_set.txt</h3>
	Contains sentences for testing and integer labels representing the language classes
	
<h5>Both the train and test files are organized as sentence - label pairs with the tab characer "\t" separating them.<h5>

<h3>chars.json</h3>
	A single json file containing two arrays: "char_to_idx" mapping characters to Integers and "idx_to_char" mapping Integers to characters

<h3>languagemap.json</h3>
	A json file mapping Integer labels to the languages they represent
  
 <h3>Source</h3>
 All sentences in this dataset were extracted from language translation files from <a href="https://manythings.org">ManyThings.org</a>
 
 <h3>Included Languages</h3>
 <ul>
  <li>English</li>
  <li>French</li>
  <li>Russian</li>
  <li>Chinese Mandarin</li>
  <li>Hebrew</li>
  <li>Portugese</li>
  <li>Polish</li>
  <li>Dutch</li>
  <li>Japanese</li>
  <li>Italian</li>
  </ul>
    <br>
 Check  <a href="https://github.com/johnolafenwa/Ling10/releases">The Release</a> to Download The datasets 
  You can reach to us via our contacts below:
  
  <br><br>
  <b>John Olafenwa</b> <br>
      <i>Website: </i>    <a style="text-decoration: none;" href="https://john.specpal.science"> https://john.specpal.science</a> <br>
      <i>Twitter: </i>    <a style="text-decoration: none;" href="https://twitter.com/johnolafenwa"> @johnolafenwa</a> <br>
      <i>Medium : </i>    <a style="text-decoration: none;" href="https://medium.com/@johnolafenwa"> @johnolafenwa</a> <br>
      <i>Facebook : </i>    <a style="text-decoration: none;" href="https://facebook.com/olafenwajohn"> olafenwajohn</a> <br>
 <br><br>
  <b>Moses Olafenwa</b> <br>
 <i>Website: </i>  <a style="text-decoration: none;" href="https://moses.specpal.science"> https://moses.specpal.science</a> <br>
 <i>Twitter: </i>    <a style="text-decoration: none;" href="https://twitter.com/OlafenwaMoses"> @OlafenwaMoses</a> <br>
      <i>Medium : </i>    <a style="text-decoration: none;" href="https://medium.com/@guymodscientist"> @guymodscientist</a> <br>
      <i>Facebook : </i>    <a style="text-decoration: none;" href="https://facebook.com/moses.olafenwa"> moses.olafenwa</a> <br>

      

</div>
