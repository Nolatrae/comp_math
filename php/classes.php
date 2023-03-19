
<?php

trait WorkDoors
{
	public function closeDoors()
    {
    	return 'Двери закрыты' . '<br>';
    }
    
    public function openDoors()
    {
    	return 'Двери открыты' . '<br>';
    }
}

interface Nickname
{
    function getNickname($nickname);
} //дать прозвище своему транспорту


class Transport
{
  public $model = 'Без названия';
  public $nomer = 'Нет номера'; 
  protected $gasMileage = 0;
    
  public function __construct($model = null, $nomer = null, $gasMileage=0)
  {
    if (isset($model))
    {
      $this->model = $model;
    }
    if (isset($nomer))
    {
      $this->nomer = $nomer;
    }
    if (isset($gasMileage))
    {
      $this->gasMileage = $gasMileage;
    }

    
  }
    
	public function getModel()
    {
    	return $this->model;
    }
    
    public function calculateDistance($CountKilometres)
    {
    	return $this->gasMileage * $CountKilometres;
    } //Высчитывает расход бензина на километры
}


class Car extends Transport implements Nickname
{

	use WorkDoors;
    
    private $countWheels = 4;
    public $nickCar = 'Без прозвища';
    
	public function doSound()
    {
    	echo 'bip-bip' . '<br>';
    }
    
    public function repairBrokenWheels($priceOneWheel)
    {
    	return $this->countWheels * $priceOneWheel;
    }
    
    
    function getNickname($nickname)
    {
        echo "Вы назвали свой автомобиль - $nickname";
        $this->nickCar = $nickname;
        #$this->nomer = $nomer;
    }
    
    
}


$Bugatti = new Car('Bugatti Veyron', '42ABC1', 10);
echo $Bugatti->model . '<br>';
echo $Bugatti->nomer . '<br>';
echo $Bugatti->getModel() . '<br>' . '<br>';


$FordFocus = new Car('FordFocus', '51BEC9', 20);
echo $FordFocus->getModel() . '<br>';
echo $FordFocus->nomer . '<br>';
$FordFocus->doSound();
echo $FordFocus->closeDoors();
echo $FordFocus->openDoors();
echo $FordFocus->repairBrokenWheels(150)  . '<br>';
echo $FordFocus->calculateDistance(100) . '<br>';
echo $FordFocus->getNickname('Ласточка') . '<br>';
echo $FordFocus->nickCar;

?>

