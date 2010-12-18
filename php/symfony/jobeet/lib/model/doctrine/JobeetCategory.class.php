<?php

/**
 * JobeetCategory
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @package    jobeet
 * @subpackage model
 * @author     Your name here
 * @version    SVN: $Id: Builder.php 6820 2009-11-30 17:27:49Z jwage $
 */
class JobeetCategory extends BaseJobeetCategory
{
  public function getActiveJobs()
  {
    $q = Doctrine_Query::create()
      ->from('JobeetJob j')
      ->where('j.category_id = ?', $this->getId());
      
    return Doctrine::getTable('JobeetJob')->getActiveJobs($q);
  }
}
