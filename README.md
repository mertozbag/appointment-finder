# appointment-finder
Appointment finder is for finding driver license appointment at USA.

Telegram bot configuration should be done before start.

In order to use it effectivelty, up-to-date webdriver is needed. 

✨ How it works? ✨

- Enters the website

- Selects current month

- Searches for defined days

- If there's a change on preferred day, it gives alert 
(Solved by Exception Handling, because it gives an error if there's a change and that's what we are looking for)

- Takes screenshot of page (In order to avoid false alert)

- Sends link of the website and screenshot via Telegram

- If there's a change or not it cleans the browser an re-opens one and starts from beginning

Developer note: Preferred days section could be done with using Loops (Also it may work better). But it created a bug while I am using it. That's why I typed the days manually. Also, it was for personal use so I didn`t spend my time on that.

