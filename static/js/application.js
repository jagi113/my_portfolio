// import 'stimulus';
// import 'stimulus-autoloader';
import '@hotwired/turbo';

const application = Application.start();
const context = require.context('./controllers', true, /\.js$/);
application.load(definitionsFromContext(context));
