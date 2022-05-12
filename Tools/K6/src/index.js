import RequestController from './controllers/request.controller.js';

const baseUrlKey = __ENV.BASE_URL;
const routeKey = __ENV.ROUTE;
const maxUsers = __ENV.MAX_USERS;

export default () => {
	const args = { baseUrlKey, routeKey };
	RequestController.testRoute(args);
};

export const options = {
	scenarios: {
		contacts: {
			executor: 'constant-vus',
			vus: maxUsers,
			duration: '5m',
			gracefulStop: '0s'
		}
	}
};
