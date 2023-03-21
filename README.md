# Media portrayal of People in STEM in Spanish written press
An analysis of the number of women and men working in Science, Technology,
Engineering and Mathematics (STEM) who are quoted in written press 
in Spain between 2016 and 2020.


### Table of Contents

1. [Project Motivation](#motivation)
2. [Background](#background)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Discussion](#discussion)
6. [Deployment](#deployment)
7. [Installation](#installation)
8. [File Descriptions](#files)
9. [Licensing](#licensing)

## Project Motivation<a name="motivation"></a>

The aim of this project is to analyze the representation of people in 
STEM (Science, Technology, Engineering and Mathematics) and related academic 
fields in Spanish press news articles. The main goal is to analyze gender 
balance/bias in Spanish media reporting writen quotes from experts 
working in STEM fields. 
The novelty of this work is that it uses an **AI-powered text 
analysis approach** that can be easily scaled-up to monitor in real time 
gender balance in quotes from experts and other content aspects with 
societal implications.

This work is my capstone project for Udacity's 
[Data Scientist](https://www.udacity.com/course/data-scientist-nanodegree--nd025) 
nanodegree.

## Background<a name="background"></a>

Diversity and inclusion in science and academia is important to ensure 
that scientific enquiry, research and innovation covers the full range 
of challenges existing in the world and society and not only those 
affecting specific human groups who have more resources or have been 
historically overprivileged and whose voices and standpoints can be 
heard more easily.

Gender bias is a prevalent issue in academic research in STEM and other 
fields where there is frequently a scarce representation of women 
([Sáinz et al 2019](https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00996/full)). 
How the media portrays the scientific and academic community, and the lack of 
role examples thereof, can influence personal career choices and deepen 
existing biases in the proportion of women and men working in specific fields. 
As repeatedly shown by previous studies, news articles usually convey 
such gender bias and underrepresentation of women when quoting  
STEM and science experts 
([Davidson et al 2023](https://elifesciences.org/reviewed-preprints/84855), 
[Fernández-Artigas et al 2022](https://dialnet.unirioja.es/servlet/articulo?codigo=8687644),
[Vico et al 2014](https://eprints.ucm.es/id/eprint/25736/)).
So far, Spanish press articles, and specifically gender bias on quotes from 
STEM experts, have not been analyzed using an automated approach 
with AI-aided Natural Language Processing, which has the potential to 
sustain a big data approach.


## Methodology<a name="methodology"></a>

[SciRide NewsMine](http://sciride.org/) 
is a huge and recently released dataset of news articles that includes several 
newspapers from Spain. Here, I analyze a random sample of **26.000 articles 
published between 2016 and 2020 of 4 major Spanish newspapers** 
(ABC, El País, El Mundo and La Vanguardia). The sample is randomized to 
include the same number of articles for each year and newspaper.

For each article, the body text is first sliced in individual sentences 
using a sentence tokenizer. Then, if the sentence contains certain 
STEM related keywords (i.e. Spanish translations of "scientist", 
"researcher", "engineer", "architect", etc. see "NLP" notebook), then 
a Named Entity Recognition analysis (using [Spacy
library](https://spacy.io/)) is run to automatically collect human names 
found in the sentence. Afterwards, each human name is assigned 
a gender using a python library called 
[Gender-Guesser](https://pypi.org/project/gender-guesser/).
3 different strategies are followed to avoid collecting the name of
the same person more than once in the same article (see "NLP" notebook).
To evaluate the quality of the analysis, both the gender assignment and
the keyword-based classification of articles (as STEM related or not STEM
related) are measured by manually reviewing a sample of 100 articles and
150 names. The predicted category is then compared with the true (manually 
assigned) category to generate a classification report including accuracy, 
precision and recall for both article classification (STEM vs no-STEM) and
gender assignment. Given the unbalanced nature of the dataset in both 
classification tasks (i.e. the low proportion of articles quoting STEM 
people and, presumably, the lower proportion of women quoted among the total 
amount of STEM poeple quoted, more about this below), a F1 maximizing 
approach has been pursued.
The proportion of STEM women and men quoted is then compared using 
Chi-square statistical tests. When multiple comparisons are done, a 
Bonferroni corrected alpha is used.

**A note about optimization**:
The keyword-based approach to article classification explained above 
included a 2-step process consisting on 'opt-in' keywords + 'opt-out' 
keywords. Only if the 'opt-in' keywords were found in a sentence, 
and if no 'opt-out' keywords were found in the same sentence, 
NER collection of human names was done 
on such sentence. Such a 2-step process was used because an earlier approach 
based solely on opt-in keywords gave a poor classification performance 
(see below). 'Opt-out' keywords were aimed to exclude sports, politics, crime 
investigations, culture, artists, and other non-STEM acitivities.

## Results<a name="results"></a>

At the article level, the approach described here has the following 
classification performance to collect articles quoting people in STEM 
(the 2 categories of the binary classifier are "STEM" and "No STEM", 
i.e., articles quoting people in STEM or articles not quoting people 
in STEM): 
- Accuracy: 0.85
- Precision (STEM): 0.78
- Precision (No STEM): 0.92
- Recall (STEM): 0.91
- Recall (No STEM): 0.81
- F1-score (STEM): 0.84
- F1-score (No STEM): 0.86

The above results are obtained when using the 2-step 'opt-in' + 'opt-out' 
keyword-based sentence selection explained in the methodology section. 
An earlier 1-step approach based solely on 'opt-in' keywords yielded a 
similar high recall but a much lower precision for the STEM article class 
(around 50% of false positive rate; while with the 2-step approach finally 
adopted, the false positive rate is around 20%).

At the level of gender assignment to names, the approach has the following 
classification performance:
- Accuracy: 0.85
- Precision (men): 1.00
- Precision (women): 0.92
- Recall (men): 0.85
- Recall (women): 0.92
- F1-score (men): 0.92
- F1-score (women): 0.92

From 26.000 articles in the analyzed sample of Spanish press articles, 
1843 articles (7.1% of total) quote at least 1 STEM person. 
The total number of unique STEM people quoted (and whose gender could be 
assigned to either man or woman) is 2637, 672 of which (25.5%)
are women and 1965 (74.5%) are men. The difference is statistically 
significant (p=0.000000).

The number of unique STEM men quoted changed across years since 2016 to 2020,
raising in 2018 and remaining at similar high values until 2020. However, the 
number of unique STEM women quoted is not statistically different when 
comparing any pair of years from 2016 to 2020.

Considering only articles quoting STEM people, men are quoted on average 
between 1.06 and 1.27 times per article, while women are quoted between 
0.36 and 0.42 times per article.

The number of articles that mention STEM women or men does not statistically 
differ between the 4 newspapers analyzed.


## Discussion<a name="discussion"></a>

The data presented here suggests that Spanish writen press quotes 
portray a **strong men-favouring gender bias in 
the representation of people working in STEM**. Moreover, despite a 
heightened awareness about the issue of gender
bias in academia and other professional fields that is occuring in 
recent years, this data does not suggest that such 
gender bias is being effectively tackled when it comes to media portrayal 
of gender representation of people in STEM. Indeed, the number of quotes 
of women in STEM has not raised significantly throghout the years analyzed 
here (from 2016 to 2020).

To the author's knowledge, this is the first and largest-scale
analysis of Spanish writen press articles done so far, made possible 
thanks to an automated AI-aided Natural Language Processing approach.

The presented work has some limitations which remain unaddressed for 
future work:
- Some quotes included in STEM quoting articles do not really 
correspond to STEM related articles but to legal or crime investigations, 
where gender bias could be higher than in STEM. 
This results from using keywords such as "investigation" 
("investigación" in Spanish, translation of "research" in English), 
which is a major keyword used to identify articles 
quoting people in STEM. Nevertheless, the overall accuracy, precision and 
recall of the approach presented here is reasonably high to support the 
conclusion that a prominent gender bias in press articles quoting 
people in STEM is indeed occuring, as already reported before in published research.
- The average number of people quoted per STEM quoting article is low (0.4 
for women, 1.3 for men). This suggests that some quotes are being missed 
by the collection process. 
- While precision of gender prediction of women names is lower than for 
men names, recall of gender prediction of women names is higher, resulting in 
the exactly same F1-score (0.92) for the prediction of both genders. 

To address all the above points and to **improve the implemented solution** 
presented here, a machine learning model could be developed in the future 
so to more reliably identify articles that quote people in STEM, 
so to complement or replace the rule-based categorization
(keyword-based) approach used here.


## Deployment <a name="deployment"></a>

A webapp has been deployed to Streamlit cloud showing a summary of the 
approach and charts with the main findings. Visit it 
[here](https://people-in-stem-in-spanish-press.streamlit.app/).


## Installation <a name="installation"></a>

To recreate the python virtual environment, use the environment.yml 
file found in the `config` folder. 
Include a dedicated python interpreter in the environment 
to avoid dependencies conflicts when installing Spacy. 
The only noteworthy customization is the use of a Spanish Spacy model 
([es_core_news_lg](https://spacy.io/models/es#es_core_news_lg)) 
for the NLP process and the python library used to automatically assign 
gender to NER-collected human names 
([Gender-Guesser](https://pypi.org/project/gender-guesser/)).

To create a python virtual environment (in Windows):
<ol>
<li>open cmd</li>
<li>cd project folder location</li>
<li>conda create --prefix ./envs</li>
<li>activate ./envs</li>
</ol>

To run Jupyter notebook inside the created virtual environment, see 
[here](https://janakiev.com/blog/jupyter-virtual-envs/).


## File Descriptions <a name="files"></a>

This repo contains the following folders and files:
- `NLP.ipynb`: jupyter notebook containing the code used to detect sentences 
quoting people in STEM and to collect human names (NER) in those sentences.
It also curates the dataset of collected names, assigns gender to those 
names and evaluates gender assignment of names and article classification 
(i.e., if the article contains at least 1 quote from a STEM person, it is 
considered as STEM related)
- `Statistics & Visualizations.ipynb`: jupyter notebook containing the code
used to run statistical comparisons and build charts
- `article_classification_evaluation.xlsx`: excel file containing the predicted 
and manually annotated article category (STEM related or not) for a ramdom 
sample of 100 articles
- `gender_classification_evaluation.xlsx`: excel file containing the predicted 
and manually annotated gender category for a random sample of 150 names 
collected by the NLP pipeline
- data: folder containing several csv files that come from the SciRide 
NewsMine dataset or are generated through the analysis. The files are:
- `sample50k_abc_mun_pai_van_wrangled_downsampled.csv (part1,part2,part3)`: 
contains the random sample of 26.000 articles from 4 newspapers
used in the analysis. It comes from an initial sample of 50.000 articles, 
which contained an unequal number of articles for the different years 
and sources, reason why it was downsampled to have a balance for all 
years and sources. 1300 articles was the highest number of the less 
frequent source-year subgroup and was then chosen as the target amount for 
downsampling. The dataset was splitted in 3 parts to keep file 
sizes within the limits allowed by GitHub.
- `sample50k_links.csv`: contains the links to all articles in the dataset
- `sample50k_articles_stats.csv`: processed dataset including the number of
women and men in STEM being quoted in each article, used in the 
'Statistics & Visualizations' notebook to build charts and statistical 
comparisons
- `sample50k_people_stats.csv`: contains a dataframe with the names of 
people in STEM being quoted in the sample of articles analyzed and 
the gender assigned to those names. It is also used in the 'Statistics & 
Visualizations' notebook to build charts and statistical comparisons
- img: folder containing several charts shown in the webapp
- config: folder containing files used to set up the python virtual 
environment ( `environment.yml`) and Spanish model in Spacy. A requirements 
file has been removed from the root repository as it gives conflicts 
when installing the webapp on Streamlit cloud (it also points to the 
same GitHub repository) 
- `app.py`: code for the Streamlit webapp 


## Licensing<a name="licensing"></a>

You can find the information about Licensing at the LICENSE file. 
For additional information, contact jviosca(at)gmail.com
