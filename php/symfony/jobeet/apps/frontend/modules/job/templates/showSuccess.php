<?php use_stylesheet('job.css') ?>
<?php use_helper('Text') ?>

<?php slot('title',
           sprintf('%s is looking for a %s', $jobeet_job->getCompany(), $jobeet_job->getPosition())) ?>

<div id="job">
  <h1><?php echo $jobeet_job->getCompany() ?></h1>
  <h2><?php echo $jobeet_job->getLocation() ?></h2>
  <h3>
    <?php echo $jobeet_job->getPosition() ?>
    <small> - <?php echo $jobeet_job->getType() ?></small>
  </h3>
  <?php if($jobeet_job->getLogo()): ?>
    <div class="logo">
      <a href="<?php echo $jobeet_job->getUrl() ?>">
        <img src="http://www.symfony-project.org/uploads/jobs/<?php echo $jobeet_job->getLogo() ?>"
          alt="<?php echo $jobeet_job->getCompany() ?> logo" />
      </a>
    </div>
  <?php endif; ?>
  
  <div class="description">
    <?php echo simple_format_text($jobeet_job->getDescription()) ?>
  </div>
  
  <h4>How to apply?</h4>
  
  <p class="how_to_apply"><?php echo $jobeet_job->getHowToApply() ?></p>
  
  <div class="meta">
    <small>posted on <?php echo $jobeet_job->getDateTimeObject('created_at')->format('m/d/Y') ?></small>
  </div>

  <hr />

  <a href="<?php echo url_for('job/edit?id='.$jobeet_job->getId()) ?>">Edit</a>
&nbsp;
  <a href="<?php echo url_for('job/index') ?>">List</a>  
</div>

