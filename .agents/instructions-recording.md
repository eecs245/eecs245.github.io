My lectures are held on Mondays and Wednesdays from 12-1:30PM. At 2:10PM, the lecture recording is available at 

https://leccap.engin.umich.edu/leccap/site/0t929w2oc176a98jk69

There are currently no recordings there, but eventually the site will look like this one, https://leccap.engin.umich.edu/leccap/site/frfru21a5l0qocuwfce (an old one), in which each new recording is a div with class="recording". In there, the div with class="date" has the recording, and the div with class="play-link" has an href attribute that, when appended to the current URL, gives the relevant link.

I'd like to build a GitHub action that, at 2:10 every M/W, opens the recording site (parameterize the review time and link at the top of the script), finds the NEWEST recording link corresponding to today's date, then goes to the correct file in _modules and adds a recording tag in the corresponding YML for that lecture with that url. So for example, if Lecture 4's link is the most recently added, then in _modules/week-03.md, we'd update

      - name: LEC 4
        type: lecture
        title: Simple Linear Regression


to

      - name: LEC 4
        type: lecture
        title: Simple Linear Regression
	recording: https://whatevergoeshere

Create the necessary artifacts in the .github folder to make the action run. Then, give me a way of testing it.
