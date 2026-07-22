# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
import os
import sys

from pyLibGDAL import defs_gdal
fields_by_layer = {}

PROJECT_PROCESSES_DIALOG_TITLE = 'Project processes'
PROCESESS_LAYER_NAME = 'processes'
PROCESESS_FIELD_LABEL = 'label'
PROCESESS_FIELD_AUTHOR = 'author'
PROCESESS_FIELD_DESCRIPTION = 'description'
PROCESESS_FIELD_DATE_TIME = 'date_time'
PROCESESS_FIELD_PROCESS_CONTENT = 'process_content'
PROCESESS_FIELD_LOG = 'log'
PROCESESS_FIELD_OUTPUT = 'output'
PROCESESS_FIELD_REMARKS = 'remarks'
# PROCESESS_FIELD_GEOMETRY = defs_gdal.LAYERS_GEOMETRY_TAG
PROCESESS_FIELD_GEOMETRY = defs_gdal.LAYERS_GEOMETRY_POSTGIS_TAG
fields_by_layer[PROCESESS_LAYER_NAME] = {}
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_LABEL] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_AUTHOR] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_DESCRIPTION] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_DATE_TIME] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_PROCESS_CONTENT] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_LOG] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_OUTPUT] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_REMARKS] = defs_gdal.type_by_name['string']
fields_by_layer[PROCESESS_LAYER_NAME][PROCESESS_FIELD_GEOMETRY] = defs_gdal.geometry_type_by_name['none']
PROCESESS_FIELD_LABEL_TAG = 'Label'
PROCESESS_FIELD_AUTHOR_TAG = 'Author'
PROCESESS_FIELD_DESCRIPTION_TAG = 'Description'
PROCESESS_FIELD_DATE_TIME_TAG = 'Date and time'
PROCESESS_FIELD_PROCESS_CONTENT_TAG = 'Process content'
PROCESESS_FIELD_LOG_TAG = 'Log'
PROCESESS_FIELD_REMARKS_TAG = 'Remarks'
PROCESESS_FIELD_OUTPUT_TAG = 'Output'
PROCESESS_FIELD_LABEL_TOOLTIP = 'Label'
PROCESESS_FIELD_AUTHOR_TOOLTIP = 'Author'
PROCESESS_FIELD_DESCRIPTION_TOOLTIP = 'Description'
PROCESESS_FIELD_DATE_TIME_TOOLTIP = 'Date and time'
PROCESESS_FIELD_PROCESS_CONTENT_TOOLTIP = 'Process content'
PROCESESS_FIELD_LOG_TOOLTIP = 'Log'
PROCESESS_FIELD_OUTPUT_TOOLTIP = 'Output'
PROCESESS_FIELD_REMARKS_TOOLTIP = 'Remarks'
project_processes_dialog_header=[PROCESESS_FIELD_LABEL_TAG,
                                 PROCESESS_FIELD_AUTHOR_TAG,
                                 PROCESESS_FIELD_DESCRIPTION_TAG,
                                 PROCESESS_FIELD_DATE_TIME_TAG,
                                 PROCESESS_FIELD_PROCESS_CONTENT_TAG,
                                 PROCESESS_FIELD_LOG_TAG,
                                 PROCESESS_FIELD_OUTPUT_TAG,
                                 PROCESESS_FIELD_REMARKS_TAG]
project_processes_dialog_field_by_header_tag = {}
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_LABEL_TAG] = PROCESESS_FIELD_LABEL
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_AUTHOR_TAG] = PROCESESS_FIELD_AUTHOR
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_DESCRIPTION_TAG] = PROCESESS_FIELD_DESCRIPTION
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_DATE_TIME_TAG] = PROCESESS_FIELD_DATE_TIME
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_PROCESS_CONTENT_TAG] = PROCESESS_FIELD_PROCESS_CONTENT
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_LOG_TAG] = PROCESESS_FIELD_LOG
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_OUTPUT_TAG] = PROCESESS_FIELD_OUTPUT
project_processes_dialog_field_by_header_tag[PROCESESS_FIELD_REMARKS_TAG] = PROCESESS_FIELD_REMARKS
project_processes_dialog_tooltip_by_header_tag = {}
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_LABEL_TAG] = PROCESESS_FIELD_LABEL_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_AUTHOR_TAG] = PROCESESS_FIELD_AUTHOR_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_DESCRIPTION_TAG] = PROCESESS_FIELD_DESCRIPTION_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_DATE_TIME_TAG] = PROCESESS_FIELD_DATE_TIME_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_PROCESS_CONTENT_TAG] = PROCESESS_FIELD_PROCESS_CONTENT_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_LOG_TAG] = PROCESESS_FIELD_LOG_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_OUTPUT_TAG] = PROCESESS_FIELD_OUTPUT_TOOLTIP
project_processes_dialog_tooltip_by_header_tag[PROCESESS_FIELD_REMARKS_TAG] = PROCESESS_FIELD_REMARKS_TOOLTIP
