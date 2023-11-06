""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import requests
from connectors.core.connector import get_logger, ConnectorError
import json
logger = get_logger('cloudflare')


class Cloudflare(object):

    def __init__(self, config):
        self.server_url = config.get('server_url').strip()
        self.account_id = config.get('account_id')
        self.zone_id = config.get('zone_id')
        self.email_id = config.get('email_id')
        self.api_key = config.get('global_api_key')
        self.headers = {
                "X-Auth-Email": self.email_id,
                "X-Auth-Key": self.api_key,
                "Content-Type": "application/json"
            }
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://{0}/'.format(self.server_url)

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        url = self.server_url + endpoint
        logger.debug('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers, data=data)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def get_list_of_block_ip_in_firewall_rule_list(config, params):
    """
        Retrieve list of all block ips in firewall rule sets.
        :param config: config
        :param params: params
        :return: List of all details,all block ips in firewall rule sets.
    """
    obj = Cloudflare(config)
    endpoint = '/client/v4/zones/{0}/firewall/rules'.format(config.get('zone_id'))
    return obj.make_api_call(endpoint, 'GET')


def get_list_firewall_rule_list(config, params):
    """
       Retrieve list of firewall rule sets.
       :param config: config
       :param params: params
       :return: List of all details,list of firewall rule sets.
    """
    obj = Cloudflare(config)
    endpoint = '/client/v4/zones/{0}/rulesets'.format(config.get('zone_id'))
    return obj.make_api_call(endpoint, 'GET')


def get_rule_id_by_rule_name(config, params):
    """
       Retrieve rule id by passing rule name.
      :param config: config
      :param params: params
      :return: List of all details, rule id by passing rule name.
    """
    obj = Cloudflare(config)
    endpoint = '/client/v4/zones/{0}/rulesets'.format(config.get('zone_id'))
    response = obj.make_api_call(endpoint, 'GET')
    if response['status'] == "Success":
        data = response['data']
        for rule in data['result']:
            if rule['name'] == params.get('ruleset_name'):
                rule_id = rule['id']
                return {'Rule ID': rule_id, 'Rule Name': params.get('ruleset_name')}
                break


def block_ip_in_firewall(config, params):
    """
       Retrieve block IP in details Cloudflare WAF.
      :param config: config
      :param params: params
      :return: List of all details,block IP in details Cloudflare WAF
    """
    obj = Cloudflare(config)
    endpoint = '/client/v4/zones/{0}/rulesets/{1}/rules'.format(config.get('zone_id'), params.get('ruleset_id'))
    payload = {
        "description": f"{params.get('description')}",
        "expression": f"(ip.src eq {params.get('ip_address')})",
        "action": "block",
        "enabled": True
    }
    return obj.make_api_call(endpoint, 'POST', data=json.dumps(payload))


def unblock_ip_in_firewall(config, params):
    """
       Retrieve unblock IP in details Cloudflare WAF.
      :param config: config
      :param params: params
      :return: List of all details,unblock IP in details Cloudflare WAF
    """
    obj = Cloudflare(config)
    endpoint = '/client/v4/zones/{0}/firewall/rules'.format(config.get('zone_id'))
    response = obj.make_api_call(endpoint, 'GET')
    if response['status'] == "Success":
        firewall_rules = response['data']
        rule_id_to_delete = None
        for rule in firewall_rules['result']:
            if rule["filter"]["expression"] == f"(ip.src eq {params.get('ip_address')})":
                rule_id_to_delete = rule["id"]
                break
        if rule_id_to_delete is not None:
            delete_endpoint = '/client/v4/zones/{0}/firewall/rules/{1}'.format(config.get('zone_id'), rule_id_to_delete)
            return  obj.make_api_call(delete_endpoint, 'DELETE')


def _check_health(config):
    try:
        obj = Cloudflare(config)
        endpoint = '/client/v4/zones/{0}/healthchecks'.format(config.get('zone_id'))
        obj.make_api_call(endpoint=endpoint, health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


operations = {
    'get_list_of_block_ip_in_firewall_rule_list': get_list_of_block_ip_in_firewall_rule_list,
    'get_list_firewall_rule_list': get_list_firewall_rule_list,
    'block_ip_in_firewall': block_ip_in_firewall,
    'get_rule_id_by_rule_name':get_rule_id_by_rule_name,
    'unblock_ip_in_firewall': unblock_ip_in_firewall
}
