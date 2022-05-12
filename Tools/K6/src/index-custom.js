import http from 'k6/http';
import { Trend } from 'k6/metrics';

const customMetric = new Trend('nova_metrica');

// Alterar comentário para definir a carga (usuários simultâneos)
const VU = __ENV.VU;

export const options = {
	scenarios: {
		contacts: {
			executor: 'constant-vus',
			vus: VU,
			duration: '5m',
			gracefulStop: '0s'
		}
	}
};

export default function () {
	const ROUTES = {
		GET: '/get',
		STREAM: '/stream/100',
		DRIP: '/drip?numbytes=5000&status=200&duration=0&delay=0'
	};

	// Alterar comentários para definir rota local (Docker) ou remota (httpbin.org)
	// const baseUrl = `http://0.0.0.0:${__ENV.PORT || DEFAULT_PORT}`;
	const baseUrl = 'http://httpbin.org';

	const requests = [
		http.get(baseUrl + ROUTES.GET),
		http.get(baseUrl + ROUTES.GET),
		http.get(baseUrl + ROUTES.STREAM),
		http.get(baseUrl + ROUTES.STREAM),
		http.get(baseUrl + ROUTES.DRIP)
	];

	requests.forEach((r) => {
		const duration = r.timings.duration;
		customMetric.add(duration);

		// Descomentar para adicionar tempo de pensamento

		// const MAX_SLEEP_TIME = 5;
		// const thinkTime = Math.round(Math.random() * MAX_SLEEP_TIME);
		// customMetric.add(thinkTime);
	});
}

// Rodar com ``k6 run <nome arquivo>.js`
