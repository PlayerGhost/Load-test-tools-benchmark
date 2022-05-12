import http from 'k6/http';
import { check, sleep } from 'k6';

const DEFAULT_PORT = 80;
export const BASE_URLS = {
	LOCAL: `http://0.0.0.0:${__ENV.PORT || DEFAULT_PORT}`,
	REMOTE: 'http://httpbin.org'
};

export const ROUTES = {
	GET: '/get',
	STREAM: '/stream/100',
	DRIP: '/drip?numbytes=5000&status=200&duration=0&delay=0'
};
const MAX_SLEEP_TIME = 5;

class RequestController {
	testRoute({ baseUrlKey, routeKey }) {
		const baseUrl = BASE_URLS[baseUrlKey];
		if (!baseUrl) {
			throw new Error(
				'Não foi definido se é uma chamada local ou remota ao httpbin!'
			);
		}

		const route = ROUTES[routeKey];
		if (!route) {
			throw new Error('Não foi definido uma rota para testar!');
		}

		const fullUrl = baseUrl.concat(route);
		const request = http.get(fullUrl);

		const expected = {};
		expected[fullUrl] = (r) => r.status === 200;

		check(request, expected);
		//this.thinkTime();
	}

	thinkTime() {
		const randomSleep = Math.round(Math.random() * MAX_SLEEP_TIME);
		// console.log(`Pensar por ${randomSleep} secs`);
		console.log(`Aguardar ${randomSleep} secs antes de nova requisição`);
		sleep(randomSleep);
	}
}

export default new RequestController();
