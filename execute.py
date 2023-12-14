from datetime import datetime
from google.cloud import aiplatform


if __name__ == '__main__':
    TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")

    job = aiplatform.PipelineJob(
        display_name="hello-world-pipeline",
        template_path="intro_pipeline_job.json",
        job_id="hello-world-pipeline-{0}".format(TIMESTAMP),
        enable_caching=False
    )

    job.submit()
    
    print('Pipeline successfully submitted')